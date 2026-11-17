import database as db
from scraper import scrape_books

def display_products(products):
    if not products:
        print("\nNo products found.")
        return
    print("\n" + "-" * 85)
    print(f"{'ID':<4} | {'Product Name':<40} | {'Price (£)':<10} | {'Availability':<15}")
    print("-" * 85)
    for p in products:
        short_name = (p[1][:37] + "...") if len(p[1]) > 40 else p[1]
        print(f"{p[0]:<4} | {short_name:<40} | {p[2]:<10.2f} | {p[3]:<15}")
    print("-" * 85)

def main():
    db.initialize_db()

    while True:
        print("\n=== E-Commerce Product Research Tool ===")
        print("1. Scrape Products from Website (Books to Scrape)")
        print("2. View All Stored Products")
        print("3. Add a Product Manually (Insert)")
        print("4. Update Product Price (Update)")
        print("5. Delete a Product (Delete)")
        print("6. Search Product by Name")
        print("7. Filter Products by Price Range")
        print("8. View Price Analytics (Cheapest, Most Expensive, Average)")
        print("9. Export Records to CSV (Bonus)")
        print("0. Exit")

        choice = input("\nEnter your choice (0-9): ").strip()

        if choice == "1":
            scrape_books(pages=2)  # Collects 40 products (20 per page)

        elif choice == "2":
            products = db.get_all_products()
            print(f"\nTotal Records in Database: {len(products)}")
            display_products(products)

        elif choice == "3":
            name = input("Enter product name: ").strip()
            try:
                price = float(input("Enter product price: "))
                availability = input("Enter availability (e.g., In stock): ").strip()
                url = input("Enter unique product URL: ").strip()
                if db.insert_product(name, price, availability, url):
                    print("Product added successfully!")
                else:
                    print("Product already exists (duplicate URL) or invalid data.")
            except ValueError:
                print("Invalid price entered. Please enter a number.")

        elif choice == "4":
            try:
                pid = int(input("Enter Product ID to update: "))
                new_price = float(input("Enter new price: "))
                if db.update_product_price(pid, new_price):
                    print("Product price updated successfully!")
                else:
                    print("Product ID not found.")
            except ValueError:
                print("Invalid input. ID must be an integer and price a number.")

        elif choice == "5":
            try:
                pid = int(input("Enter Product ID to delete: "))
                if db.delete_product(pid):
                    print("Product deleted successfully!")
                else:
                    print("Product ID not found.")
            except ValueError:
                print("Invalid Product ID.")

        elif choice == "6":
            keyword = input("Enter product name keyword to search: ").strip()
            results = db.search_by_name(keyword)
            display_products(results)

        elif choice == "7":
            try:
                min_p = float(input("Enter minimum price: "))
                max_p = float(input("Enter maximum price: "))
                results = db.filter_by_price(min_p, max_p)
                display_products(results)
            except ValueError:
                print("Please enter valid numeric values for price.")

        elif choice == "8":
            cheapest, expensive, avg = db.get_price_analytics()
            if cheapest and expensive:
                print("\n--- Price Analytics ---")
                print(f"Cheapest Product      : {cheapest[0]} (£{cheapest[1]:.2f})")
                print(f"Most Expensive Product: {expensive[0]} (£{expensive[1]:.2f})")
                print(f"Average Product Price : £{avg:.2f}")
            else:
                print("Database is empty. Please scrape or add products first.")

        elif choice == "9":
            db.export_to_csv()

        elif choice == "0":
            print("Exiting application. Goodbye!")
            break

        else:
            print("Invalid choice. Please select between 0 and 9.")

if __name__ == "__main__":
    main()
