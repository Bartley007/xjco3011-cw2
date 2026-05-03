# Quote Search Engine

A CLI-based search engine for [Quotes to Scrape](https://quotes.toscrape.com/), built for XJCO3011 Coursework 2.

---

## Architecture Overview

```
                    ┌─────────────┐
                    │ quotes.     │
                    │ toscrape.com│
                    └──────┬──────┘
                           │ HTTP (6s politeness window)
                    ┌──────▼──────┐
                    │   Crawler   │  requests + BeautifulSoup
                    │  crawler.py │
                    └──────┬──────┘
                           │ extracted quotes (text, author, tags, url)
                    ┌──────▼──────┐
                    │   Indexer   │  regex tokenisation → lowercase
                    │  indexer.py │  defaultdict(term → doc_id → positions)
                    └──────┬──────┘
                           │ JSON serialisation
                    ┌──────▼──────┐
                    │ data/       │
                    │ index.json  │  inverted index
                    │ docs.json   │  document store
                    └──────┬──────┘
                           │ JSON deserialisation
                    ┌──────▼──────┐
                    │   Searcher  │  set.intersection AND queries
                    │  search.py  │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  CLI (main) │  REPL: build/load/find/print/exit
                    │  main.py    │
                    └─────────────┘
```

## Features

- **Web Crawler**: Crawls all 10 pages of quotes.toscrape.com with configurable politeness delay (6s production, 0.1s debug).
- **Inverted Index Builder**: Constructs a positional inverted index recording term frequency and exact word positions within each document.
- **Boolean AND Search**: Implements set-intersection multi-word queries — returns only documents containing ALL query terms.
- **Interactive CLI**: REPL-style shell with four commands: `build`, `load`, `print`, `find`.
- **Persistence**: Index and documents serialised to JSON for fast reloading without re-crawling.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Run the main script:

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

### Example Session

```
> load
Successfully loaded index with 100 quotes.
Unique vocabulary: 836 terms

> find life
Found 16 matching quotes (showing first 2):

[1] "“Life is what happens when you're busy making other plans.”"
    — John Lennon
    Tags: life, living

[2] "“The purpose of our lives is to be happy.”"
    — Dalai Lama
    Tags: happiness, life, living

> find love world
Boolean intersection — 3 matching quotes:

[1] "...the more I see of the world, the more am I dissatisfied with it..."
    — Jane Austen

[2] "I am good, but not an angel... a small girl in a big world trying to find someone to love"
    — Marilyn Monroe

> find xyzxyzxyz
No matching quotes found.

> print wisdom
Index entry for 'wisdom':
  Total Frequency:  1
  Document Count:   1
  Doc 37: positions [4]

> exit
```

## Inverted Index Structure

The inverted index is stored as a nested dictionary:

```
{
    "word": {
        "<doc_id>": [<position1>, <position2>, ...],
        ...
    },
    ...
}
```

- **Key (outer)**: Lowercased word token.
- **Key (inner)**: Document ID (0-indexed).
- **Value**: List of word positions within that document.

**Example** — the quote "Life is what happens when you're busy making other plans" would produce entries like:
- `"life"` → `{0: [0]}` (appears at position 0 in document 0)
- `"busy"` → `{0: [6]}` (appears at position 6)

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
├── requirements.txt    Python dependencies
└── README.md           This file
```

## Testing

Run the full test suite:

```bash
python -m pytest tests/ -v
```

### Test Coverage

| Test File | Tests | What It Covers |
|-----------|-------|---------------|
| `test_search.py` | 4 | Single-word, multi-word AND, non-existent word, empty query |
| `test_indexer.py` | 2 | Index construction, save-and-load roundtrip |
| `test_crawler.py` | 2 | Initialisation parameters, DEBUG delay config |

All 8 tests pass with no external network dependency (crawler tests use mock HTTP responses).

## GenAI Usage Declaration

### Tool Used

- **AI Tool**: Windsurf (Cascade)
- **Category**: Green — AI has an integral role (per XJCO3011 Coursework 2 guidelines)

### How AI Was Used

1. **API Familiarisation (High value)**:
   Asked AI for concise examples of BeautifulSoup selectors and the requests.Session API. The official documentation is verbose; AI examples saved approximately 2 hours of reading time.

2. **Data Structure Design (Medium value)**:
   AI suggested the nested `defaultdict(lambda: defaultdict(list))` pattern for the inverted index. This was the correct choice — it lazily creates inner dicts when adding new word-document pairs, reducing boilerplate significantly.

3. **Search Algorithm Implementation (Low value — required debugging)**:
   The AI's initial `find()` implementation used naive list operations and did not account for JSON serialisation converting integer dict keys to strings. This caused a silent bug where loaded indexes failed to match documents. **I had to debug and fix this myself** by converting keys back to integers in `load_index()`.

### Critical Evaluation

| Aspect | Assessment |
|--------|-----------|
| **Code Quality** | AI output was clean and PEP8-compliant, with type hints. However, correctness suffered — the type conversion bug was non-obvious. |
| **Time Saved** | Approximately 3 hours on boilerplate, documentation reading, and file structure. |
| **Learning Impact** | The debugging phase (fixing the key-type bug) taught me more about how posting lists actually work than if I had written everything from scratch. |
| **Limitations** | AI could not evaluate architectural trade-offs (e.g., combined-field indexing vs. per-field indexing). Only human judgement can make those decisions. |

### Reflection

> "The AI was a productive assistant, but not a substitute for understanding. Every line of AI-generated code was manually reviewed and, where necessary, corrected. The most valuable learning came not from what AI got right, but from fixing what it got wrong."

---

*Coursework 2 — XJCO3011 Web Services and Web Data*  
*Student: Minhao Gao (201691058)*  
*GitHub: [Bartley007/xjco3011-cw2](https://github.com/Bartley007/xjco3011-cw2)*
