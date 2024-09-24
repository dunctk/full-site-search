import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import advertools as adv
import requests_cache
import argparse
import csv
import pandas as pd

# Cache requests to avoid redundant network calls
requests_cache.install_cache('site_cache')

# List of websites to crawl
SITES = ["https://www.resonio.com", "https://www.resonio.de"]

# List of text phrases to search for in the crawled data
TEXT_TO_SEARCH = ["free screening questions", "kostenlose Screening-Fragen"]

def crawl_sites(sites):
    """
    Crawl the given list of sites and save the crawled data to JSON lines files.
    """
    for site in tqdm(sites, desc="Crawling sites"):
        # Generate output file name based on the site URL
        output_file = f"{site.replace('https://', '').replace('http://', '').replace('/', '_')}_crawl.jl"
        # Use advertools to crawl the site and save the data
        adv.crawl(site, follow_links=True, output_file=output_file)

def search_terms_in_crawled_data(sites, search_terms):
    """
    Search for the given terms in the crawled data of the sites.
    """
    crawled_data = []
    for site in tqdm(sites, desc="Searching terms in crawled data"):
        # Generate the file name of the crawled data
        crawl_file = f"{site.replace('https://', '').replace('http://', '').replace('/', '_')}_crawl.jl"
        # Read the crawled data from the JSON lines file
        crawl_result = pd.read_json(crawl_file, lines=True)
        for term in tqdm(search_terms, desc=f"Searching terms in {site}"):
            for _, row in crawl_result.iterrows():
                # Check if the term is in the body text of the crawled data
                if 'body_text' in row and term.lower() in row['body_text'].lower():
                    # Append the site, term, and URL to the results
                    crawled_data.append((site, term, row['url']))
    return crawled_data

def save_to_csv(data, filename="search_results.csv"):
    """
    Save the search results to a CSV file.
    """
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(["Site", "Search Term", "URL"])
        # Write the data rows
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    # Set up argument parser for command line options
    parser = argparse.ArgumentParser(description="Crawl and search sites.")
    parser.add_argument('--crawl', action='store_true', help="Perform crawling of the sites")
    args = parser.parse_args()

    # If the --crawl argument is provided, perform crawling
    if args.crawl:
        crawl_sites(SITES)

    # Search for the terms in the crawled data
    crawled_data = search_terms_in_crawled_data(SITES, TEXT_TO_SEARCH)
    # Save the search results to a CSV file
    save_to_csv(crawled_data)

    # Print the search results
    for data in crawled_data:
        print(f"Found '{data[1]}' in {data[0]} at {data[2]}")

