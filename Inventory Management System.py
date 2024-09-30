# Class for Product
class Product:
    def __init__(self, product_id, name, price, quantity, low_stock_threshold):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.low_stock_threshold = low_stock_threshold

    def display_product_info(self):
        print(f"ID: {self.product_id}, Name: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}, Low Stock Threshold: {self.low_stock_threshold}")

    def is_low_stock(self):
        return self.quantity < self.low_stock_threshold

# Class for Inventory Management System
class Inventory:
    def __init__(self):
        self.products = {}

    # Add a new product to the inventory
    def add_product(self, product_id, name, price, quantity, low_stock_threshold):
        if product_id in self.products:
            print(f"Product ID {product_id} already exists.")
        else:
            new_product = Product(product_id, name, price, quantity, low_stock_threshold)
            self.products[product_id] = new_product
            print(f"Product '{name}' added successfully.")

    # Edit an existing product
    def edit_product(self, product_id, name=None, price=None, quantity=None, low_stock_threshold=None):
        if product_id in self.products:
            product = self.products[product_id]
            if name:
                product.name = name
            if price:
                product.price = price
            if quantity:
                product.quantity = quantity
            if low_stock_threshold:
                product.low_stock_threshold = low_stock_threshold
            print(f"Product ID {product_id} has been updated.")
        else:
            print(f"Product ID {product_id} not found.")

    # Delete a product from the inventory
    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print(f"Product ID {product_id} has been deleted.")
        else:
            print(f"Product ID {product_id} not found.")

    # View all products
    def view_products(self):
        if self.products:
            for product in self.products.values():
                product.display_product_info()
        else:
            print("No products in inventory.")

    # Check for low stock products
    def check_low_stock(self):
        low_stock_products = [product for product in self.products.values() if product.is_low_stock()]
        if low_stock_products:
            print("\nLow Stock Products:")
            for product in low_stock_products:
                product.display_product_info()
        else:
            print("No low stock products.")

    # Generate sales summary
    def sales_summary(self):
        total_sales_value = sum((product.price * (product.low_stock_threshold - product.quantity)) for product in self.products.values() if product.quantity < product.low_stock_threshold)
        print(f"\nTotal Sales Summary: ${total_sales_value:.2f}")

# Main Program
def main():
    inventory = Inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Edit Product")
        print("3. Delete Product")
        print("4. View All Products")
        print("5. Check Low Stock")
        print("6. Generate Sales Summary")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            low_stock_threshold = int(input("Enter low stock threshold: "))
            inventory.add_product(product_id, name, price, quantity, low_stock_threshold)

        elif choice == '2':
            product_id = input("Enter product ID to edit: ")
            name = input("Enter new product name (or leave blank to keep current): ")
            price = input("Enter new product price (or leave blank to keep current): ")
            quantity = input("Enter new product quantity (or leave blank to keep current): ")
            low_stock_threshold = input("Enter new low stock threshold (or leave blank to keep current): ")

            inventory.edit_product(
                product_id, 
                name=name if name else None, 
                price=float(price) if price else None, 
                quantity=int(quantity) if quantity else None, 
                low_stock_threshold=int(low_stock_threshold) if low_stock_threshold else None
            )

        elif choice == '3':
            product_id = input("Enter product ID to delete: ")
            inventory.delete_product(product_id)

        elif choice == '4':
            inventory.view_products()

        elif choice == '5':
            inventory.check_low_stock()

        elif choice == '6':
            inventory.sales_summary()

        elif choice == '7':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
