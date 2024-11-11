import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="subhradeep3",
)

cursor = mydb.cursor()

db_cursor = mydb.cursor()
db_cursor.execute("CREATE DATABASE IF NOT EXISTS sales_inventory")
db_cursor.execute("use sales_ln")

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255))")
cursor.execute("CREATE TABLE IF NOT EXISTS items (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price DECIMAL(10, 2), quantity INT)")

# Set default username and password
cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")

# Function to verify login credentials
def login(username, password):
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    if user:
        return True
    else:
        return False

# Function to add an item
def add_item(name, price, quantity):
    cursor.execute("INSERT INTO items (name, price, quantity) VALUES (%s, %s, %s)", (name, price, quantity))
    mydb.commit()

# Function to remove an item
def remove_item(item_id):
    cursor.execute("DELETE FROM items WHERE id = %s", (item_id,))
    mydb.commit()

# Function to update the price of an item
def update_price(item_id, price):
    cursor.execute("UPDATE items SET price = %s WHERE id = %s", (price, item_id))
    mydb.commit()

# Function to update the quantity of an item
def update_quantity(item_id, quantity):
    cursor.execute("UPDATE items SET quantity = %s WHERE id = %s", (quantity, item_id))
    mydb.commit()

# Function to display all items
def display_items():
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    for item in items:
        print(f"ID: {item[0]}, Name: {item[1]}, Price: {item[2]}, Quantity: {item[3]}")

# Function to change password
def change_password(username, new_password):
    cursor.execute("UPDATE users SET password = %s WHERE username = %s", (new_password, username))
    mydb.commit()

# Main program loop
while True:
    print("Sales Inventory Management System")
    print("1. Login")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        if login(username, password):
            print("Login successful!")
            while True:
                print("1. Add Item")
                print("2. Remove Item")
                print("3. Update Price")
                print("4. Update Quantity")
                print("5. Display Items")
                print("6. Change Password")
                print("7. Logout")
                sub_choice = input("Enter your choice: ")

                if sub_choice == "1":
                    name = input("Enter item name: ")
                    price = float(input("Enter item price: "))
                    quantity = int(input("Enter item quantity: "))
                    add_item(name, price, quantity)
                    print("Item added successfully!")

                elif sub_choice == "2":
                    item_id = int(input("Enter item ID: "))
                    remove_item(item_id)
                    print("Item removed successfully!")

                elif sub_choice == "3":
                    item_id = int(input("Enter item ID: "))
                    price = float(input("Enter new price: "))
                    update_price(item_id, price)
                    print("Price updated successfully!")

                elif sub_choice == "4":
                    item_id = int(input("Enter item ID: "))
                    quantity = int(input("Enter new quantity: "))
                    update_quantity(item_id, quantity)
                    print("Quantity updated successfully!")

                elif sub_choice == "5":
                    display_items()

                elif sub_choice == "6":
                    new_password = input("Enter new password: ")
                    change_password(username, new_password)
                    print("Password changed successfully!")

                elif sub_choice == "7":
                    break

                else:
                    print("Invalid choice!")

        else:
            print("Invalid username or password!")

    elif choice == "2":
        break

    else:
        print("Invalid choice!")