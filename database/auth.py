import sqlite3



def user_auth(email, password):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM User_Information WHERE email = ? AND password = ?", (email, password))
    user = cursor.fetchone()
    conn.close()

    return user