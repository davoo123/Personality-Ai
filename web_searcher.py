"""
Web Search and Information Gathering Module
"""
import requests
import time
import json
import random
from bs4 import BeautifulSoup
from typing import List, Dict, Any, Optional
import wikipedia
from googlesearch import search
from urllib.parse import urljoin, urlparse
from config import *
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

class WebSearcher:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        self.search_history = []
        
    def search_google(self, query: str, num_results: int = 5) -> List[Dict[str, str]]:
        """Search Google and return results"""
        try:
            console.print(f"🔍 Searching Google for: [cyan]{query}[/cyan]")
            
            results = []
            search_results = search(query, num_results=num_results, stop=num_results, pause=2)
            
            for url in search_results:
                try:
                    content = self.extract_content_from_url(url)
                    if content:
                        results.append({
                            'url': url,
                            'title': content.get('title', 'No title'),
                            'content': content.get('text', '')[:1000],  # First 1000 chars
                            'source': 'google'
                        })
                        time.sleep(1)  # Be respectful to servers
                except Exception as e:
                    console.print(f"[yellow]Could not extract from {url}: {e}[/yellow]")
                    continue
                    
            return results
            
        except Exception as e:
            console.print(f"[red]Google search error: {e}[/red]")
            return []
            
    def search_wikipedia(self, query: str) -> List[Dict[str, str]]:
        """Search Wikipedia for information"""
        try:
            console.print(f"📚 Searching Wikipedia for: [cyan]{query}[/cyan]")
            
            # Search for pages
            search_results = wikipedia.search(query, results=3)
            results = []
            
            for title in search_results:
                try:
                    page = wikipedia.page(title)
                    results.append({
                        'url': page.url,
                        'title': page.title,
                        'content': page.summary[:1000],  # First 1000 chars of summary
                        'source': 'wikipedia'
                    })
                except wikipedia.exceptions.DisambiguationError as e:
                    # Try the first option from disambiguation
                    try:
                        page = wikipedia.page(e.options[0])
                        results.append({
                            'url': page.url,
                            'title': page.title,
                            'content': page.summary[:1000],
                            'source': 'wikipedia'
                        })
                    except:
                        continue
                except:
                    continue
                    
            return results
            
        except Exception as e:
            console.print(f"[red]Wikipedia search error: {e}[/red]")
            return []
            
    def extract_content_from_url(self, url: str) -> Optional[Dict[str, str]]:
        """Extract text content from a URL"""
        try:
            response = self.session.get(url, timeout=TIMEOUT)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
                
            # Get title
            title = soup.find('title')
            title_text = title.get_text().strip() if title else "No title"
            
            # Get main content
            # Try to find main content areas
            content_selectors = [
                'article', 'main', '.content', '#content', 
                '.post-content', '.entry-content', 'p'
            ]
            
            text_content = ""
            for selector in content_selectors:
                elements = soup.select(selector)
                if elements:
                    text_content = ' '.join([elem.get_text().strip() for elem in elements])
                    break
                    
            if not text_content:
                text_content = soup.get_text()
                
            # Clean up text
            lines = (line.strip() for line in text_content.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text_content = ' '.join(chunk for chunk in chunks if chunk)
            
            return {
                'title': title_text,
                'text': text_content,
                'url': url
            }
            
        except Exception as e:
            console.print(f"[yellow]Could not extract content from {url}: {e}[/yellow]")
            return None
            
    def comprehensive_search(self, query: str) -> List[Dict[str, str]]:
        """Perform comprehensive search across multiple sources"""
        all_results = []
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            
            # Search Wikipedia
            task1 = progress.add_task("Searching Wikipedia...", total=None)
            wiki_results = self.search_wikipedia(query)
            all_results.extend(wiki_results)
            progress.remove_task(task1)
            
            # Search Google
            task2 = progress.add_task("Searching Google...", total=None)
            google_results = self.search_google(query, num_results=SEARCH_RESULTS_LIMIT)
            all_results.extend(google_results)
            progress.remove_task(task2)
            
        # Record search in history
        self.search_history.append({
            'query': query,
            'timestamp': time.time(),
            'results_count': len(all_results)
        })
        
        console.print(f"✅ Found {len(all_results)} results for: [green]{query}[/green]")
        return all_results
        
    def extract_key_information(self, search_results: List[Dict[str, str]], topic: str) -> Dict[str, Any]:
        """Extract and organize key information from search results"""
        key_info = {
            'topic': topic,
            'definitions': [],
            'key_concepts': [],
            'examples': [],
            'interesting_facts': [],
            'sources': [],
            'timestamp': time.time()
        }
        
        for result in search_results:
            content = result.get('content', '').lower()
            title = result.get('title', '')
            
            # Extract definitions (sentences with "is", "are", "means", "refers to")
            sentences = content.split('.')
            for sentence in sentences:
                if any(word in sentence for word in ['is', 'are', 'means', 'refers to', 'defined as']):
                    if len(sentence.strip()) > 20 and len(sentence.strip()) < 200:
                        key_info['definitions'].append(sentence.strip())
                        
            # Extract key concepts (capitalized words, technical terms)
            words = content.split()
            for i, word in enumerate(words):
                if word.istitle() and len(word) > 3:
                    context = ' '.join(words[max(0, i-2):i+3])
                    if len(context) > 10:
                        key_info['key_concepts'].append(context)
                        
            # Look for examples
            for sentence in sentences:
                if any(word in sentence for word in ['example', 'for instance', 'such as', 'including']):
                    if len(sentence.strip()) > 20:
                        key_info['examples'].append(sentence.strip())
                        
            # Collect interesting facts (sentences with numbers, percentages, studies)
            for sentence in sentences:
                if any(indicator in sentence for indicator in ['%', 'study', 'research', 'found that', 'discovered']):
                    if len(sentence.strip()) > 30:
                        key_info['interesting_facts'].append(sentence.strip())
                        
            # Record source
            key_info['sources'].append({
                'title': title,
                'url': result.get('url', ''),
                'source_type': result.get('source', 'unknown')
            })
            
        # Remove duplicates and limit results
        key_info['definitions'] = list(set(key_info['definitions']))[:5]
        key_info['key_concepts'] = list(set(key_info['key_concepts']))[:10]
        key_info['examples'] = list(set(key_info['examples']))[:5]
        key_info['interesting_facts'] = list(set(key_info['interesting_facts']))[:5]
        
        return key_info
        
    def get_search_statistics(self) -> Dict[str, Any]:
        """Get search statistics"""
        return {
            'total_searches': len(self.search_history),
            'recent_searches': self.search_history[-5:] if self.search_history else [],
            'average_results_per_search': sum(s['results_count'] for s in self.search_history) / len(self.search_history) if self.search_history else 0
        }
