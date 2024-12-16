import sqlite3

# Функция для инициализации базы данных (создание таблицы и добавление данных)
def initiate_db():
    # Подключаемся к базе данных (если базы нет, она будет создана)
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    # Создаем таблицу (если она еще не существует)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        price INTEGER NOT NULL
    )
    ''')

    # Добавляем продукты в таблицу, если она пустая
    cursor.execute('''
    SELECT COUNT(*) FROM Products
    ''')
    result = cursor.fetchone()

    # Если таблица пуста, добавляем начальные данные
    if result[0] == 0:
        add_product('Logitech G102', 'Мышь с сенсором 8000 DPI', 10000)
        add_product('Logitech G304', 'Беспроводная игровая мышь', 15000)
        add_product('Logitech G PRO', 'Мышь для профессиональных игроков', 20000)
        add_product('ARDOR GAMING Fury', 'Игровая мышь с подсветкой', 25000)

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()

# Функция для добавления продукта в таблицу
def add_product(title, description, price):
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    # Вставляем продукт в таблицу
    cursor.execute('''
    INSERT INTO Products (title, description, price) VALUES (?, ?, ?)
    ''', (title, description, price))

    connection.commit()
    connection.close()

# Функция для получения всех продуктов из базы данных
def get_all_products():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    cursor.execute('SELECT title, description, price FROM Products')
    products = cursor.fetchall()

    connection.close()
    return products



