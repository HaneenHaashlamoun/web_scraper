# web_scraper

https://github.com/HaneenHaashlamoun/web_scraper/pulls/1

## Feature Tasks and Requirements
- [x] Scrape a Wikipedia page and record which passages need citations.
- [x] E.g. History of Mexico has a few “citations needed”.
- [x] Your web scraper should report the number of citations needed.
- [x] Your web scraper should identify those cases AND include the relevant passage.
- [x] E.g. Citation needed for “lorem spam and impsum eggs”
- [x] Consider the “relevant passage” to be the parent element that contains the passage, often a paragraph element.

## Implementation Notes
- [x] Count function must be named get_citations_needed_count
- [x] get_citations_needed takes in a url and returns an integer
- [x] Report function must be named get_citations_needed_report
- [x] get_citations_needed_report takes in a url and returns a string
- [x] the string should be formatted with each citation needed on own line, in order found.
- [x] Module must be named scraper.py