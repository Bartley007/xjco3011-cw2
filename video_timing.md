# CW2 Video — Full Timeline & Subtitle Script

**Student**: Minhao Gao (201691058)
**Total Duration**: 5:00 (strict)

---

## Recording Segments

| Part | Content | Screen Recording | Duration |
|:----:|---------|-----------------|:--------:|
| **A** | Live Demo | Terminal: `python demo.py` | 2:00 |
| **B** | Code Walkthrough | VS Code: browse `src/` files | 1:30 |
| **C** | Testing | Terminal: `python -m pytest tests/ -v` | 0:30 |
| **D** | Version Control | Terminal: `git --no-pager log --oneline` | 0:30 |
| **E** | GenAI Reflection | Face cam / voiceover only | 0:30 |
| | **Total** | | **5:00** |

---

## Part A — Live Demo (Run `python demo.py`, 2:00)

| Time | Screen | Voiceover |
|:----:|--------|-----------|
| 0:00 | Project header | *(pause, wait for title to appear)* |
| 0:05 | `> load` — index loaded | "First, I load the pre-built inverted index from disk. It was previously built by crawling 10 pages of quotes.toscrape.com — 100 quotes with over 800 unique terms. The index is stored in JSON format and read back into memory instantly." |
| 0:25 | `> find life` — 2 results shown | "Now a single-word search for 'life'. The engine looks up the term in the inverted index, retrieves all matching document IDs, and returns the quote content with author and tags." |
| 0:45 | `> find love world` — 3 results | "This is a multi-word AND query. The searcher finds documents containing BOTH 'love' AND 'world' using boolean intersection. Only three quotes satisfy both conditions — this intersection is the core search algorithm." |
| 1:05 | `> find xyzxyzxyz` — empty result | "Edge case: searching for a word that doesn't exist. The engine returns an empty result gracefully — no crash, no error, handled by the short-circuit logic in the intersection algorithm." |
| 1:20 | `> print wisdom` — index internals | "The 'print' command reveals the inverted index internals: total frequency, document count, and exact word positions. This positional data enables fast full-text lookups." |
| 1:40 | `> build` — simulated crawl output | "Finally, the build command. The crawler visits each page with a 6-second politeness window, extracts quotes via BeautifulSoup, builds the inverted index with positional tracking, and saves to disk." |
| 1:55 | Summary line | "That covers all four commands — build, load, print, and find — with single-word queries, multi-word queries, and edge case handling." |
| 2:00 | *(cut away)* | *(Part A ends)* |

---

## Part B — Code Walkthrough (Record separately, 1:30)

> Open VS Code, browse `src/` files in order: `crawler.py` → `indexer.py` → `search.py` → `main.py`

| Time | Screen | Voiceover |
|:----:|--------|-----------|
| 2:00 | Show `src/crawler.py` | "Let me walk through the code. The crawler uses the requests library with a Session object for connection reuse. It starts from page 1, follows the next-page link, and extracts quotes via BeautifulSoup selectors. A DEBUG flag controls the delay — 0.1 seconds for development, 6 seconds for production to respect the politeness window." |
| 2:25 | Scroll to `src/indexer.py` | "The indexer is the core component. The inverted index is a nested defaultdict — outer key is the word, mapped to a dict of document IDs mapped to lists of positions. I concatenate text, author, and tags for combined-field indexing, which simplifies queries but sacrifices field-specific search. Tokenization uses regex to extract alphanumeric sequences and lowercase everything." |
| 2:55 | Scroll to `src/search.py` | "The search engine implements boolean AND intersection. For each query term, it retrieves the set of document IDs. If any term is missing, it short-circuits to empty. It then uses set.intersection to find common documents. One trade-off: results are returned in document ID order without relevance ranking. The positional data is available for future phrase-search or proximity features." |
| 3:15 | Scroll to `src/main.py` | "The CLI is a REPL loop handling build, load, print, find, and exit. The searcher object is lazy-initialised — available only after build or load, with guard checks that print clear error messages if you try to search first." |
| 3:30 | *(cut away)* | *(Part B ends)* |

---

## Part C — Testing (Record separately, 0:30)

> Terminal: `python -m pytest tests/ -v`

| Time | Screen | Voiceover |
|:----:|--------|-----------|
| 3:30 | Pytest running | "Now let me show the test suite. I have three test files covering each module." |
| 3:35 | 7 passed | "The search tests cover single-word lookup, multi-word AND intersection, non-existent words, and empty queries. The indexer tests verify correct word-to-document mapping and save-and-load round-trips. The crawler test validates the DEBUG delay configuration. All 7 tests pass. If I had more time, I would strengthen the crawler test with full mock HTML pages." |
| 4:00 | *(cut away)* | *(Part C ends)* |

---

## Part D — Version Control (Record separately, 0:30)

> Terminal: `git --no-pager log --oneline`

| Time | Screen | Voiceover |
|:----:|--------|-----------|
| 4:00 | Git log appears | "Here is the Git commit history. I followed a feature-first workflow — each module got its own commit, followed by tests, documentation, and refinement. Commit messages use conventional prefixes: feat, test, docs, chore." |
| 4:15 | Scroll through commits | "The logical progression is clear: web crawler first, then the indexer, search engine, CLI, unit tests, documentation, and final polish. This demonstrates incremental, well-structured development. The repository is on GitHub at github.com/Bartley007/xjco3011-cw2." |
| 4:30 | *(cut away)* | *(Part D ends)* |

---

## Part E — GenAI Critical Evaluation (Voiceover only, 0:30)

> No screen needed — face cam or pure voiceover

| Time | Screen | Voiceover |
|:----:|--------|-----------|
| 4:30 | Black screen or face cam | "This project used AI assistance under the University's Green category. AI was most helpful for two things: understanding BeautifulSoup's API with concise working examples, and suggesting the nested defaultdict structure for the inverted index, which turned out clean and effective." |
| 4:45 | Same | "However, the AI-generated search code needed significant rework. The initial suggestion used naive list operations without handling JSON string-to-integer type conversion, causing silent bugs. I had to debug and fix that myself — which deepened my understanding of how posting lists work. The real learning came from fixing what AI got wrong. I am confident in every line because I verified and modified every piece myself." |
| 5:00 | End | *(Video ends)* |

---

## Quick Reference: Recording Commands

| Part | Action | Command | Duration |
|:----:|--------|---------|:--------:|
| **A** | Run demo script | `python demo.py` | 2:00 |
| **B** | Browse source code in VS Code | — | 1:30 |
| **C** | Run tests | `python -m pytest tests/ -v` | 0:30 |
| **D** | Show Git history | `git --no-pager log --oneline` | 0:30 |
| **E** | Voiceover only | — | 0:30 |

---

**Tip**: Record Parts A~E separately, then stitch them together. Each part's timing is independent, so if one take goes long, you can re-record just that segment.
