import sqlite3

def delete_specific_user(userID):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM User_Information WHERE user_id = ?", (userID,))
    user = cursor.fetchone()

    if user is None:
        conn.close()
        return f"please enter correct user_id."

    cursor.execute("DELETE FROM User_Information WHERE user_id = ?", (userID,))
    conn.commit()
    conn.close()
    return f"This user_id deleted successfully."


def delete_all_users():
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM User_Information")
    conn.commit()
    conn.close()

    return "All users deleted successfully."


def delete_specific_product(product_id):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Admin_Product WHERE product_id = ?", (product_id,))
    product = cursor.fetchone()

    if product is None:
        conn.close()
        return f"please enter correct product_id."

    cursor.execute("DELETE FROM Admin_Product WHERE product_id = ?", (product_id,))
    conn.commit()
    conn.close()
    return f"This product_id {product_id} deleted successfully."


def delete_all_products():
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Admin_Product")
    conn.commit()
    conn.close()

    return "All products deleted successfully."



def delete_specific_userStock(product_id):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM User_Stock WHERE product_id = ?", (product_id,))
    product = cursor.fetchone()

    if product is None:
        conn.close()
        return f"please enter correct product_id."

    cursor.execute("DELETE FROM User_Stock WHERE product_id = ?", (product_id,))
    conn.commit()
    conn.close()
    return f"This product_id {product_id} deleted successfully."


def delete_all_userStock():
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM User_Stock")
    conn.commit()
    conn.close()

    return "All UserProduct deleted successfully."


def delete_specific_userOrder(order_id):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM User_Order WHERE order_id = ?", (order_id,))
    product = cursor.fetchone()

    if product is None:
        conn.close()
        return f"please enter correct order_id."

    cursor.execute("DELETE FROM User_Order WHERE order_id = ?", (order_id,))
    conn.commit()
    conn.close()
    return f"This order_id {order_id} deleted successfully."


def delete_all_userOrder():
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM User_Order")
    conn.commit()
    conn.close()

    return "All User Orders deleted successfully."


