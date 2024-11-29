import sqlite3

connection = sqlite3.connect('telebot_data.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute("""CREATE TABLE IF NOT EXISTS Users (
                        id INTEGER PRIMERY KEY,
                        username TEXT NOT NULL,
                        email TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        balance INTEGER NOT NULL
                        )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS Products (
                        id INTEGER PRIMERY KEY,
                        title TEXT NOT NULL,
                        description TEXT,
                        price INTEGER NOT NULL
                    )""")
    connection.commit()
initiate_db()


cursor.execute('DELETE FROM Products')
for num in range(1, 5):
    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                   (f'Продукт {num}', f'Описание {num}', num*100))
    connection.commit()

def get_all_products():
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()

def add_user(username, email, age):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, 1000)",
                   (username, email, age))
    connection.commit()

def is_included(username):
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    for user in users:
        if user[1] == username:
            return True
    return False