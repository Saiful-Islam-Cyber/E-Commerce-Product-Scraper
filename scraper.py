import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from database import insert_product


def scrape_books(pages=2):
    added_count = 0
    skipped_count = 0

    sub = "books."
    domain = "toscrape.com"
    path = "/catalogue/page-"

    for page in range(1, pages + 1):
        url = "https://" + sub + domain + path + str(page) + ".html"
        print(f"Scraping page {page}: {url} ...")

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Failed to fetch page {page}: {e}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("article", class_="product_pod")

        for book in books:
            try:
                title_tag = book.h3.a
                name = title_tag["title"].strip()

                relative_url = title_tag["href"]
                product_url = urljoin(url, relative_url)

                price_text = book.find("p", class_="price_color").text.strip()
                price = float(price_text.replace("£", "").replace("Â", ""))

                availability = book.find("p", class_="instock availability").text.strip()

                if insert_product(name, price, availability, product_url):
                    added_count += 1
                else:
                    skipped_count += 1

            except (AttributeError, ValueError) as parse_err:
                print(f"Skipping a malformed product entry: {parse_err}")

        time.sleep(1)

    print(f"\nScraping finished! New products added: {added_count}, Duplicates skipped: {skipped_count}")
