"""Pre-build the index for demo purposes."""
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from crawler import QuoteCrawler
from indexer import QuoteIndexer

print('=' * 50)
print('Step 1: Crawling quotes.toscrape.com ...')
print('=' * 50)
crawler = QuoteCrawler()
quotes = crawler.crawl_all_quotes()
print(f'Success! Crawled {len(quotes)} quotes.')

print()
print('=' * 50)
print('Step 2: Building inverted index (TF-IDF) ...')
print('=' * 50)
indexer = QuoteIndexer(data_dir=os.path.join(os.path.dirname(__file__), 'data'))
indexer.build_index(quotes)
indexer.save_index()
print(f'Done! Index saved with {len(indexer.documents)} documents.')
print(f'Index file: data/index.json')
print(f'Docs file: data/docs.json')
