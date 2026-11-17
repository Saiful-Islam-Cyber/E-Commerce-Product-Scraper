# E-Commerce Product Scraper & SQL Database

This is a Python command-line application designed to collect product information from online stores and organize it into a local SQLite database for market analysis, combining web scraping (`requests`, `BeautifulSoup`) with relational database management (`sqlite3`).

## Target Website
- **Source:** [Books to Scrape](https://toscrape.com)
- A sandbox environment for web scraping practice. The scraper collects data from the first two catalog pages (40 products) with a 1-second delay between requests.

## Core Features
- **Data Collection:** Scrapes book titles, numeric prices, availability, and product links.
- **Duplicate Prevention:** Uses a `UNIQUE` constraint on `product_url` with `INSERT OR IGNORE`.
- **Database Management (CRUD):** Add, view, update prices by ID, and delete records.
- **Search & Filtering:** Search by keywords or filter by a price range.
- **Price Analytics:** Uses SQL (`ORDER BY` with `LIMIT 1` and `AVG`) to find the cheapest, most expensive, and average prices.
- **CSV Export:** Exports data to `products_export.csv`.

## Project Structure
```text
E-Commerce-Product-Scraper/
├── database.py           # SQLite setup, CRUD, and analytics queries
├── scraper.py            # Web scraping logic and rate limiting
├── main.py               # Interactive CLI menu
├── products.db           # SQLite database file
├── products_export.csv   # Exported CSV dataset
├── requirements.txt      # Python dependencies
├── Screenshots/          # Output screenshots (scraping, tables, analytics)
└── README.md             # Project documentation
```

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Saiful-Islam-Cyber/E-Commerce-Product-Scraper.git
   cd E-Commerce-Product-Scraper
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## How to Use

1. Run the application:
   ```bash
   python main.py
   ```
2. Select **Option 1** to scrape products and populate `products.db`.
3. Use **Options 2 through 9** to view, search, filter, analyze, or export your data.

## Sample Output Screenshots

### 1. Web Scraping & Data Collection
![Scraping Output](Screenshots/scraping_output.png)

### 2. Stored Products & Price Filter
![Product Table Output](Screenshots/product_table.png)

### 3. SQL Price Analytics
![Price Analytics Output](Screenshots/price_analytics.png)

## Notes on Error Handling
- Network exceptions are managed via `requests.RequestException` to prevent crashes.
- CLI inputs are validated using `try-except` blocks.
