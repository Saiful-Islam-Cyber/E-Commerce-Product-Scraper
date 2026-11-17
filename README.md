# E-Commerce Product Scraper & Market Research Tool

This is a Python command-line application built to collect product details from an online store and organize them into a local SQLite database for basic market research. The project combines web scraping (`requests` and `BeautifulSoup`) with relational database management (`sqlite3`).

## Target Website
- **Source:** [Books to Scrape](https://toscrape.com)
- This site is a publicly available sandbox specifically created for practicing web scraping. The scraper collects data from the first two catalog pages (40 products in total) while adding a 1-second delay between page requests to avoid overloading the server.

## What This Tool Does
- **Data Collection:** Fetches book titles, prices (converted to numeric values), stock availability, and individual product page links.
- **Duplicate Handling:** Uses a `UNIQUE` constraint on the `product_url` column along with `INSERT OR IGNORE` so running the scraper multiple times does not create duplicate entries.
- **Database Management (CRUD):** Supports adding new products manually, viewing all saved records, updating prices by product ID, and deleting records.
- **Search & Price Filtering:** Allows searching products using partial keywords and filtering items within a minimum and maximum price range.
- **Price Summary:** Uses SQL queries (`ORDER BY` with `LIMIT 1` and `AVG`) to find the cheapest book, the most expensive book, and the average price across the dataset.
- **CSV Export:** Exports all records from the SQLite database into a `products_export.csv` file for viewing in Excel or Google Sheets.

## Project Structure
```text
E-Commerce-Product-Scraper/
├── database.py           # SQLite table setup, CRUD functions, search, and analytics queries
├── scraper.py            # Web scraping logic with error handling and rate limiting
├── main.py               # Interactive CLI menu to run all operations
├── products.db           # SQLite database file containing the scraped records
├── products_export.csv   # Exported CSV file generated from the database
├── requirements.txt      # Required third-party Python packages
├── Screenshots/          # Output screenshots showing scraping, queries, and analytics
└── README.md             # Project documentation
```

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Saiful-Islam-Cyber/E-Commerce-Product-Scraper.git
   cd E-Commerce-Product-Scraper
   ```

2. **Install the required libraries:**
   Make sure Python 3 is installed, then run:
   ```bash
   pip install -r requirements.txt
   ```
   *(Only `requests` and `beautifulsoup4` are external packages; `sqlite3` and `csv` come built-in with Python.)*

## How to Use

1. Start the program from the terminal:
   ```bash
   python main.py
   ```
2. Choose **Option 1** first to scrape 40 products from the website and save them into `products.db`.
3. Once data is stored, use **Options 2 to 9** from the menu to view records, add/update/delete items, search by name, filter by price, check price analytics, or export the table to CSV.

## Notes on Error Handling
- Network issues or invalid HTTP responses during scraping are caught using `requests.RequestException` so the program does not crash unexpectedly.
- Invalid user inputs (such as entering text instead of numbers for prices or product IDs) are handled with `try-except` blocks to keep the menu running smoothly.
