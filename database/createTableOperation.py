import sqlite3

def create_tables():
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    # User_Information Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS User_Information (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id VARCHAR(255),
            password VARCHAR(255),
            level INT,
            date_of_account_creation DATE,
            isApproved BOOLEAN,
            block BOOLEAN,
            name VARCHAR(255),
            email VARCHAR(255),
            phone_number VARCHAR(255),
            pinCode VARCHAR(255),
            address VARCHAR(255)
        );
    ''')

    # Admin_Product Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Admin_Product (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id VARCHAR(255),
            product_name VARCHAR(255),
            product_image TEXT,
            price REAL,
            category VARCHAR(255),
            stock INTEGER,
            expire_date DATE
        );
    ''')

    # User_Order Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS User_Order (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id VARCHAR(255),
            product_id VARCHAR(255),
            order_status BOOLEAN,
            product_name VARCHAR(255),
            price REAL,
            category VARCHAR(255),
            expire_date DATE,
            quantity INTEGER
        );
    ''')

    # User_Stock Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS User_Stock (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id VARCHAR(255),
            product_name VARCHAR(255),
            category VARCHAR(255),
            expire_date DATE,
            price REAL,
            stock INTEGER
        );
    ''')

    # Sell_History Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Sell_History (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sell_id VARCHAR(255),
            product_id VARCHAR(255),
            quantity INTEGER,
            remaining_stock INTEGER,
            date_of_sell DATE,
            total_amount REAL,
            price REAL,
            product_name VARCHAR(255),
            user_name VARCHAR(255),
            user_id VARCHAR(255)
        );
    ''')

    conn.commit()
    conn.close()

# Function call (optional)
# create_tables()
