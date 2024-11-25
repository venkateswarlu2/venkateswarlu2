import threading
import requests
from bs4 import BeautifulSoup
import csv
import logging

# Configure logging (adjust severity level as needed)
logging.basicConfig(filename='scraping.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all heading elements (h1, h2, h3)
        elements = soup.find_all(['h1', 'h2', 'h3', 'p', 'head', 'title', 'body', 'image'])

        if elements:
            with open('scraped_data.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                # Assuming header is already written, comment out if needed
                writer.writerow(['Web Scraping'])  # Write header only if not already present
                for element in elements:
                    writer.writerow([element.text.strip()])
                    logging.info(f"Scraped heading: {element.text.strip()} from {url}")
        else:
            logging.warning(f"No heading elements (h1, h2, h3) found on {url}")

    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching {url}: {e}")

urls = [
    #'https://www.google.com/',
    'https://github.com/krishnaik06/Perfect-Roadmap-To-Learn-Data-Science-In-2024?tab=readme-ov-file',
    
]

threads = []
for url in urls:
    thread = threading.Thread(target=scrape_website, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

logging.info("Scraping completed. See scraping.log for details.")