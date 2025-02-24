import sqlite3


def update_userOrder(orderID, **keyword):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    for key, value in keyword.items():
        cursor.execute(f"UPDATE User_Order SET {key} = ? WHERE order_id = ?", (value, orderID))

    conn.commit()
    conn.close()


def update_userDetails(userID, **ketword):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    for key, value in ketword.items():
        if key == "name":
            cursor.execute("UPDATE User_Information SET name = ? WHERE user_id = ?", (value, userID))
        elif key == "password":
            cursor.execute("UPDATE User_Information SET password = ? WHERE user_id = ?", (value, userID))
        elif key == "email":
            cursor.execute("UPDATE User_Information SET email = ? WHERE user_id = ?", (value, userID))
        elif key == "isApproved":
            cursor.execute("UPDATE User_Information SET isApproved = ? WHERE user_id = ?", (value, userID))
        elif key == "block":
            cursor.execute("UPDATE User_Information SET block = ? WHERE user_id = ?", (value, userID))
        elif key == "phone_number":
            cursor.execute("UPDATE User_Information SET phone_number = ? WHERE user_id = ?", (value, userID))
        elif key == "pinCode":
            cursor.execute("UPDATE User_Information SET pinCode = ? WHERE user_id = ?", (value, userID))
        elif key == "address":
            cursor.execute("UPDATE User_Information SET address = ? WHERE address = ?", (value, userID))
        
    conn.commit()
    conn.close()

def check_userId_exists(userID):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM User_Information WHERE user_id = ?", (userID,))
    user_exests = cursor.fetchone()[0] > 0

    conn.close()
    return user_exests

def update_productDetails(productID, **ketword):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    for key, value in ketword.items():
        if key == "product_name":
            cursor.execute("UPDATE Admin_Product SET product_name = ? WHERE product_id = ?", (value, productID))
        elif key == "product_image":
            cursor.execute("UPDATE Admin_Product SET product_image = ? WHERE product_id = ?", (value, productID))
        elif key == "price":
            cursor.execute("UPDATE Admin_Product SET price = ? WHERE product_id = ?", (value, productID))
        elif key == "category":
            cursor.execute("UPDATE Admin_Product SET category = ? WHERE product_id = ?", (value, productID))
        elif key == "stock":
            cursor.execute("UPDATE Admin_Product SET stock = ? WHERE product_id = ?", (value, productID))
        elif key == "expire_date":
            cursor.execute("UPDATE Admin_Product SET expire_date = ? WHERE product_id = ?", (value, productID))

    conn.commit()
    conn.close()

def check_productId_exists(productId):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM Admin_Product WHERE product_id = ?", (productId,))
    user_exests = cursor.fetchone()[0] > 0

    conn.close()
    return user_exests
