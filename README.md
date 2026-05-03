# Quote Search Engine
A CLI-based search engine for [Quotes to Scrape](https://quotes.toscrape.com/), built for XJCO3011 Coursework 2.
## Features

- **Web Crawler**: Crawls all 10 pages with configurable politeness delay (6s production, 0.1s debug).
- **Inverted Index Builder**: Positional index recording term frequency and word positions per document.
- **Boolean AND Search**: Set-intersection multi-word queries returning documents containing ALL query terms.
- **Interactive CLI**: REPL with four commands: `build`, `load`, `print`, `find`.
- **Persistence**: Index and documents serialised to JSON for fast reloading.
## Installation
```bash
pip install -r requirements.txt
```
## Usage
```bash
python src/main.py
```
### Commands

| Command | Description | Example |
|---------|-------------|---------|
| `build` | Crawl website and build the inverted index | `> build` |
| `load` | Load a previously saved index from disk | `> load` |
| `find <words...>` | Search for quotes containing all words (AND) | `> find love world` |
| `print <word>` | Display the inverted index entry for a word | `> print wisdom` |
| `exit` | Quit the application | `> exit` |

### Example

```
> load
Successfully loaded index with 100 quotes.  Unique vocabulary: 836 terms
> find life
Found 16 matching quotes.  First: "Life is what happens when you're busy making other plans." — John Lennon
> find love world
Boolean intersection — 3 quotes.  E.g. "...a small girl in a big world trying to find someone to love" — Marilyn Monroe
> find xyzxyzxyz
No matching quotes found.
> print wisdom
Index entry for 'wisdom':  Total Frequency: 1  Document Count: 1  Doc 37: positions [4]
> exit
```
## Project Structure
```
cw2/
├── src/
│   ├── crawler.py      Web crawler (requests + BeautifulSoup)
│   ├── indexer.py      Inverted index builder (defaultdict, JSON)
│   ├── search.py       Search engine (boolean intersection)
│   └── main.py         Interactive CLI (REPL loop)
├── tests/
│   ├── test_crawler.py Crawler unit tests (mock HTTP)
│   ├── test_indexer.py Indexer tests (build, save, load roundtrip)
│   └── test_search.py  Search tests (single/multi-word, edge cases)
├── data/
│   ├── index.json      Serialized inverted index (37 KB, 836 terms)
│   └── docs.json       Document store (24 KB, 100 quotes)
├── requirements.txt
└── README.md
```
## Inverted Index Structure
```
{"word": {"<doc_id>": [<position1>, <position2>, ...], ...}, ...}
```
The index is a nested dictionary: outer key is the lowercased word token, inner key is the document ID, and the value is a list of zero-indexed word positions. All three fields (quote text, author, tags) are combined into one index, simplifying queries at the cost of field-specific search.
## Testing
```bash
python -m pytest tests/ -v
```
| Test File | Tests | What It Covers |
|-----------|-------|---------------|
| `test_search.py` | 4 | Single-word, multi-word AND, non-existent word, empty query |
| `test_indexer.py` | 2 | Index construction, save-and-load roundtrip |
| `test_crawler.py` | 2 | Initialisation parameters, DEBUG delay config |
All 8 tests pass with no external network dependency.
## GenAI Usage Declaration
- **Tool**: Windsurf (Cascade) — Green category per XJCO3011 guidelines.
### How AI Was Used
1. **API Familiarisation (High value)**: AI provided concise BeautifulSoup and requests.Session examples, saving ~2 hours of documentation reading.
2. **Data Structure Design (Medium value)**: AI suggested the nested `defaultdict(lambda: defaultdict(list))` pattern for the inverted index. This correctly reduces boilerplate when adding new word-document pairs.
3. **Search Algorithm Implementation (Low value — required debugging)**: The AI's initial `find()` did not account for JSON converting integer keys to strings, causing a silent bug on reload. I had to debug and fix this by converting keys back to integers in `load_index()`.

### Critical Evaluation
| Aspect | Assessment |

|--------|-----------|
| **Code Quality** | PEP8-compliant with type hints, but correctness suffered — the type conversion bug was non-obvious. |
| **Time Saved** | ~3 hours on boilerplate, docs reading, and file scaffolding. |
| **Learning Impact** | Debugging the key-type bug taught me more about posting list mechanics than writing from scratch. |
| **Limitations** | AI cannot evaluate architectural trade-offs (e.g., combined-field vs. per-field indexing). Only human judgement can make those decisions. |

**Reflection**: The AI was a productive assistant, but not a substitute for understanding. Every line of AI-generated code was manually reviewed and corrected where necessary. The most valuable learning came not from what AI got right, but from fixing what it got wrong.
---
*Coursework 2 — XJCO3011 Web Services and Web Data*  
*Student: Minhao Gao (201691058)*  
*GitHub: [Bartley007/xjco3011-cw2](https://github.com/Bartley007/xjco3011-cw2)*
