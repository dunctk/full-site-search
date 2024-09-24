# Website Text Search Tool

## Overview

This tool allows you to search for specific text phrases across one or more websites. It is useful for various purposes, such as:

- **Content Verification**: Ensuring that specific phrases or keywords are present on your website.
- **SEO Audits**: Checking if important keywords are used across your site.
- **Compliance Checks**: Verifying that required legal or compliance text is present on all pages.
- **Competitive Analysis**: Searching for specific content on competitor websites.

The tool uses web crawling to gather data from the specified websites and then searches the crawled data for the given text phrases. The results are saved to a CSV file for easy analysis.

## Requirements

- Python 3.x
- Required Python packages (install via `pip`):
  - `requests`
  - `beautifulsoup4`
  - `tqdm`
  - `advertools`
  - `requests-cache`
  - `argparse`
  - `pandas`

## Installation

1. Clone the repository or download the script.
2. Install the required Python packages:
   ```bash
   pip install requests beautifulsoup4 tqdm advertools requests-cache argparse pandas
   ```

## Usage

### Crawling Websites

To crawl the specified websites, use the `--crawl` argument:

```bash
python search.py --crawl
```

This will crawl the websites listed in the `SITES` variable and save the crawled data to JSON lines files.

### Searching for Text Phrases

To search for the specified text phrases in the crawled data, simply run the script without any arguments:

```bash
python search.py
```

This will search for the phrases listed in the `TEXT_TO_SEARCH` variable in the crawled data and save the results to a CSV file named `search_results.csv`.

### Example

1. Crawl the websites:
   ```bash
   python search.py --crawl
   ```

2. Search for the text phrases:
   ```bash
   python search.py
   ```

3. Check the `search_results.csv` file for the results.

## Configuration

You can configure the list of websites to crawl and the text phrases to search for by modifying the `SITES` and `TEXT_TO_SEARCH` variables in the `search.py` script:

```python
SITES = ["https://www.example.com", "https://www.example2.com"]
TEXT_TO_SEARCH = ["example phrase", "another example phrase"]
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any questions or inquiries, please contact [duncan@innermaps.org].
