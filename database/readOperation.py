import sqlite3
import json

def getAllUsers():
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM User_Information")
    users = cursor.fetchall()
    conn.close()

    userJson = [
        {
            "id": user[0],
            "user_id": user[1],
            "password": user[2],
            "level": user[3],
            "date_of_account_creation": user[4],
            "isApproved": user[5],
            "block": user[6],
            "name": user[7],
            "email": user[8],
            "phone_number": user[9],
            "pinCode": user[10],
            "address": user[11],
        }
        for user in users
    ]

    return userJson


def getAllProduct():
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Admin_Product")
    products = cursor.fetchall()
    conn.close()

    productjson = [
        {
            "id": product[0],
            "product_id": product[1],
            "product_name": product[2],
            "product_image": product[3],
            "price": product[4],
            "category": product[5],
            "stock": product[6],
            "expire_date": product[7]
        }
        for product in products
    ]

    return productjson


def getAllStock():
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM User_Stock")
    products = cursor.fetchall()
    conn.close()

    productjson = [
        {
            "id": product[0],
            "product_id": product[1],
            "product_name": product[2],
            "category": product[3],
            "expire_date": product[4],
            "price": product[5],
            "stock": product[6]
        }
        for product in products
    ]

    return productjson


def getAllUserOrders():
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM User_Order")
    orderProducts = cursor.fetchall()
    conn.close()

    orderProductjson = [
        {
            "id": orderProduct[0],
            "order_id": orderProduct[1],
            "product_id": orderProduct[2],
            "order_status": orderProduct[3],
            "product_name": orderProduct[4],
            "price": orderProduct[5],
            "category": orderProduct[6],
            "expire_date": orderProduct[7],
            "quantity": orderProduct[8]
        }
        for orderProduct in orderProducts
    ]

    return orderProductjson


def getSpecificUser(userID):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM User_Information WHERE user_id = ?", (userID,))
    user = cursor.fetchone()
    conn.close()

    if user is None:
        return None

    return {
        "id": user[0],
        "user_id": user[1],
        "password": user[2],
        "level": user[3],
        "date_of_account_creation": user[4],
        "isApproved": user[5],
        "block": user[6],
        "name": user[7],
        "email": user[8],
        "phone_number": user[9],
        "pinCode": user[10],
        "address": user[11]
    }


def getSpecificProduct(productID):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Admin_Product WHERE product_id = ?", (productID,))
    product = cursor.fetchone()
    cursor.close()
    
    if product is None:
        return None
    
    return {
        "id": product[0],
        "product_id": product[1],
        "product_name": product[2],
        "product_image": product[3],
        "price": product[4],
        "category": product[5],
        "stock": product[6],
        "expire_date": product[7]
    }
