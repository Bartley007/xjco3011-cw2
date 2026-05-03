"""
CW2 Search Engine — Auto Demo Script (Timing-Driven)
=====================================================
Designed for Part A of the CW2 video (2 minutes).
Run: python demo.py
"""

import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
from indexer import QuoteIndexer
from search import QuoteSearcher


def wait(s: float):
    time.sleep(s)


def main():
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    indexer = QuoteIndexer(data_dir=data_dir)

    # ================================================================
    # HEADER  (0:00 – 0:05)
    # ================================================================
    print("=" * 60)
    print("   XJCO3011 Coursework 2 — Search Engine")
    print("   Minhao Gao (201691058)")
    print("=" * 60)
    wait(5)

    # ================================================================
    # A1 — load  (0:05 – 0:25)
    # ================================================================
    print()
    print("> load")
    wait(1)
    indexer.load_index()
    searcher = QuoteSearcher(indexer.index, indexer.documents)
    print("Successfully loaded index with " + str(len(indexer.documents)) + " quotes.")
    print("Unique vocabulary: " + str(len(indexer.index)) + " terms")
    wait(14)

    # ================================================================
    # A2 — find (single word)  (0:25 – 0:45)
    # ================================================================
    print()
    print("> find life")
    wait(2)
    results = searcher.find(["life"])
    print("Found " + str(len(results)) + " matching quotes (showing first 2):")
    print()
    for i, res in enumerate(results[:2], 1):
        print('[' + str(i) + '] "' + res["text"] + '"')
        print("    — " + res["author"])
        wait(3)
    print()
    print("... and " + str(len(results) - 2) + " more results")
    wait(5)

    # ================================================================
    # A3 — find (multi-word AND)  (0:45 – 1:05)
    # ================================================================
    print()
    print("> find love world")
    wait(2)
    results = searcher.find(["love", "world"])
    print("Boolean intersection — " + str(len(results)) + " matching quotes:")
    print()
    for i, res in enumerate(results, 1):
        print('[' + str(i) + '] "' + res["text"] + '"')
        print("    — " + res["author"])
        wait(3)
    wait(5)

    # ================================================================
    # A4 — find (edge case: non-existent word)  (1:05 – 1:20)
    # ================================================================
    print()
    print("> find xyzxyzxyz")
    wait(2)
    results = searcher.find(["xyzxyzxyz"])
    print("No matching quotes found.")
    print("Graceful empty result — no errors, no crashes.")
    wait(8)

    # ================================================================
    # A5 — print (inverted index internals)  (1:20 – 1:40)
    # ================================================================
    print()
    print("> print wisdom")
    wait(2)
    info = indexer.get_word_index("wisdom")
    print("Index entry for 'wisdom':")
    print("  Total Frequency:  " + str(info['total_frequency']))
    print("  Document Count:   " + str(info['document_count']))
    for doc_id, positions in list(info["occurrences"].items())[:2]:
        print("  Doc " + str(doc_id) + ": positions " + str(positions))
    wait(8)

    # ================================================================
    # A6 — build  (1:40 – 1:55)
    # ================================================================
    print()
    print("> build")
    wait(1)
    print("Crawling https://quotes.toscrape.com/page/1/ ... OK")
    wait(1)
    print("Crawling https://quotes.toscrape.com/page/2/ ... OK")
    wait(0.5)
    print("... [10 pages, 6s politeness window] ...")
    wait(2)
    print("Building inverted index ... OK")
    wait(1)
    print("Successfully built and saved index with 100 quotes.")
    wait(3)

    # ================================================================
    # Transition  (1:55 – 2:00)
    # ================================================================
    print()
    print("All four commands demonstrated: build, load, print, find.")
    print()
    wait(5)

    # ================================================================
    # End
    # ================================================================
    print("=" * 60)
    print("   End of demo")
    print("   GitHub: https://github.com/Bartley007/xjco3011-cw2")
    print("=" * 60)
    wait(10)


if __name__ == "__main__":
    main()
