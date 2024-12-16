import sqlite3

def initiate_db():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        price INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
    SELECT COUNT(*) FROM Products
    ''')
    result = cursor.fetchone()

    if result[0] == 0:
        add_product('Logitech G102', 'Мышь с сенсором 8000 DPI', 10000)
        add_product('Logitech G304', 'Беспроводная игровая мышь', 15000)
        add_product('Logitech G PRO', 'Мышь для профессиональных игроков', 20000)
        add_product('ARDOR GAMING Fury', 'Игровая мышь с подсветкой', 25000)

    connection.commit()
    connection.close()

def add_product(title, description, price):
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    cursor.execute('''
    INSERT INTO Products (title, description, price) VALUES (?, ?, ?)
    ''', (title, description, price))

    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    cursor.execute('SELECT title, description, price FROM Products')
    products = cursor.fetchall()

    connection.close()
    return products



