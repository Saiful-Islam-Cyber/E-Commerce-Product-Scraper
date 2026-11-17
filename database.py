import sqlite3
import csv

DB_NAME = "products.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def initialize_db():
    """Creates the products table if it does not exist."""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                availability TEXT NOT NULL,
                product_url TEXT UNIQUE NOT NULL
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database initialization error: {e}")
    finally:
        conn.close()

def insert_product(name, price, availability, product_url):
    """Inserts a new product, ignoring duplicates based on product_url."""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR IGNORE INTO products (name, price, availability, product_url)
            VALUES (?, ?, ?, ?)
        ''', (name, price, availability, product_url))
        conn.commit()
        return cursor.rowcount > 0  # Returns True if a new row was inserted
    except sqlite3.Error as e:
        print(f"Error inserting product: {e}")
        return False
    finally:
        conn.close()

def get_all_products():
    """Retrieves all products from the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, price, availability, product_url FROM products")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_by_name(keyword):
    """Searches products matching the keyword."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE name LIKE ?", (f"%{keyword}%",))
    rows = cursor.fetchall()
    conn.close()
    return rows

def filter_by_price(min_price, max_price):
    """Filters products within a given price range."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE price BETWEEN ? AND ?", (min_price, max_price))
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_product_price(product_id, new_price):
    """Updates the price of a specific product by ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
    conn.commit()
    updated = cursor.rowcount > 0
    conn.close()
    return updated

def delete_product(product_id):
    """Deletes a product record by ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    deleted = cursor.rowcount > 0
    conn.close()
    return deleted

def get_price_analytics():
    """Returns cheapest product, most expensive product, and average price."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT name, price FROM products ORDER BY price ASC LIMIT 1")
    cheapest = cursor.fetchone()
    
    cursor.execute("SELECT name, price FROM products ORDER BY price DESC LIMIT 1")
    most_expensive = cursor.fetchone()
    
    cursor.execute("SELECT AVG(price) FROM products")
    avg_price = cursor.fetchone()[0]
    
    conn.close()
    return cheapest, most_expensive, avg_price

def export_to_csv(filename="products_export.csv"):
    """Bonus: Exports all database records to a CSV file."""
    products = get_all_products()
    if not products:
        print("No data available to export.")
        return
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Product Name", "Price (£)", "Availability", "Product URL"])
        writer.writerows(products)
    print(f"Successfully exported {len(products)} records to {filename}!")
