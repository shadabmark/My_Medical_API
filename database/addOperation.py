import sqlite3
import uuid
from datetime import date

def create_user(name, password, phone_number, email, pin_code, address):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    user_id = str(uuid.uuid4())
    date_of_account_creation = date.today()

    cursor.execute("""
        INSERT INTO User_Information (user_id, password, level, date_of_account_creation, isApproved, block, name, email, phone_number, pinCode, address)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (user_id, password, 1, date_of_account_creation, 0, 0, name, email, phone_number, pin_code, address))

    conn.commit()
    conn.close()

    return user_id  

def create_product(product_name, product_image, price, category, stock, expire_date):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    product_id = str(uuid.uuid4())

    cursor.execute("""
        INSERT INTO Admin_Product (product_id, product_name, product_image, price, category, stock, expire_date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (product_id, product_name, product_image, price, category, stock, expire_date))

    conn.commit()
    conn.close()

    return product_id

def create_user_stock(product_id, product_name, category, expire_date, price, stock):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO User_Stock (product_id, product_name, category, expire_date, price, stock)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (product_id, product_name, category, expire_date, price, stock))

    conn.commit()
    conn.close()

    return product_id

def order_product(product_name, product_id, price, category, expire_date, quantity):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    order_id = str(uuid.uuid4())

    cursor.execute("""
        INSERT INTO User_Order (order_id, product_id, order_status, product_name, price, category, expire_date, quantity)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (order_id, product_id, 0, product_name, price, category, expire_date, quantity))

    conn.commit()
    conn.close()

    return order_id
