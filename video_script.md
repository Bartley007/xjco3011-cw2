# CW2 视频完整配音脚本

**学生**: Minhao Gao (201691058)
**总时长**: ~5 分钟

---

## Part A — Live Demonstration（~2 分钟）

> 对应画面：终端操作演示

**[load]**
"First, I'll start by loading the pre-built inverted index from disk. The index was built by crawling quotes.toscrape.com — 10 pages, 100 quotes in total. The load command reads the index file and document store back into memory, and I'm ready to search."

**[find life — 单次查询]**
"Now a single-word search for 'life'. The engine looks up the term in the inverted index and returns all documents containing it. You can see the matched quote text, the author, and the associated tags."

**[find love world — 多词 AND 查询]**
"This is the important part — a multi-word query for 'love' AND 'world'. The searcher applies boolean intersection: it finds the posting list for each word, then returns only documents that appear in ALL of them. This is the core search mechanism that powers most search engines."

**[find xyzxyzxyz — 边界情况]**
"Now for an edge case — searching for a word that doesn't exist in the index. The engine correctly returns no matches. This shows the system handles non-existent terms gracefully without errors."

**[print wisdom — 索引结构]**
"Next, the 'print' command shows the internal structure of the inverted index. For the word 'wisdom', we can see its total frequency across all documents, how many documents contain it, and the exact word positions in each document. This positional information would enable phrase searching in the future."

**[build — 构建索引]**
"Finally, the build command. The crawler visits each page of quotes.toscrape.com with a 6-second politeness window between requests. It extracts each quote's text, author, and tags using BeautifulSoup. Then the indexer tokenises the text, converts everything to lowercase, and builds the inverted index with positional tracking. The result is saved to disk."

---

## Part B — Code Walkthrough & Design Decisions（~1.5 分钟）

> 对应画面：依次展示 `crawler.py` → `indexer.py` → `search.py` → `main.py` 代码

**[crawler.py]**
"Let me walk through the architecture. The crawler uses Python's requests library with a Session object to maintain persistent connections. It starts from page 1, finds the next-page link in the HTML, and continues until no more pages exist. There's a DEBUG flag that gives me a 0.1-second delay during development, versus the required 6-second politeness window for production runs. Each quote is extracted via BeautifulSoup selectors — the text, author, and tags are stored as a structured dict."

**[indexer.py]**
"The indexer is the heart of the project. The inverted index is implemented as a nested defaultdict — the outer key is the word, mapped to an inner dict of document IDs mapped to lists of positions. When building the index, I concatenate the quote text, author, and tags into a single string and tokenise it with a regex that extracts alphanumeric sequences and lowercases everything. This combined-field approach simplifies query logic — a search for 'einstein' will match both the author name and any quote content — but the trade-off is you can't restrict searches to a specific field."

**[search.py]**
"The search engine implements boolean AND intersection. For each query word, it retrieves the set of document IDs from the index. If any word is missing, it short-circuits and returns empty. Otherwise it uses Python's set.intersection to find documents containing ALL terms. One design trade-off here: the current implementation returns results in document ID order without relevance ranking. A production system would add TF-IDF scoring or BM25 ranking. The positional data stored in the index is available for implementing phrase queries and proximity search in future extensions."

**[main.py]**
"The CLI is a simple REPL loop. It handles four commands — build, load, print, find — plus exit. The searcher object is lazily initialised: it becomes available only after a successful build or load command, with error messages if you try to search before loading the index."

---

## Part C — Testing Demonstration（~30 秒）

> 对应画面：运行 `python -m pytest tests/ -v`

"Now let me show the test suite. I have three test files covering each module."

[运行测试，等结果出现]

"The search tests cover single-word queries, multi-word AND intersection queries, non-existent words, and empty queries — all pass. The indexer tests verify that the index builds correctly with the right word-to-document mappings, and that save-and-load round-trips preserve data integrity. The crawler test validates initialisation parameters, including the DEBUG delay configuration."

"Overall, the tests cover the core functionality and edge cases. If I had more time, I would extend the crawler test with full mock HTML pages and add property-based tests for the indexer with random quote data."

---

## Part D — Version Control（~30 秒）

> 对应画面：运行 `git --no-pager log --oneline`

"Here's my Git commit history for this project."

[显示日志]

"I followed a feature-first workflow: each core module — crawler, indexer, searcher, CLI — got its own commit. Then I added tests, documentation, and refinement commits. The commit messages use conventional commit prefixes like 'feat', 'test', 'docs', and 'chore' to make the purpose of each change clear. The repository is hosted on GitHub at github.com slash Bartley007 slash xjco3011-cw2, with the full commit history and README documentation."

---

## Part E — GenAI Critical Evaluation（~30 秒）

"This project used AI assistance under the University's Green category guidelines. I'd like to critically reflect on that experience."

"AI was most helpful in two areas: first, understanding BeautifulSoup's API — the documentation can be dense, and AI gave me concise working examples that I could adapt. Second, the AI helped structure the inverted index data model, suggesting the nested defaultdict approach which turned out to be clean and effective."

"However, the AI-generated search code needed significant modification. The initial suggestion used simple list intersections without handling the JSON string-to-integer type conversion, which caused silent bugs. I had to debug and fix that myself, which deepened my understanding of how the posting lists actually work under the hood."

"On reflection, using AI accelerated the initial prototyping phase, but the real learning came when I had to understand and fix what it generated. I'm confident in every line of code in this project because I've verified and modified it myself. The balance between AI speed and manual understanding was the key lesson from this process."

---

> 全片结束
