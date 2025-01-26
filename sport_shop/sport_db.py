import sqlite3

# Функция для создания базы данных и таблиц
def create_database():
    conn = sqlite3.connect('sport.db')
    c = conn.cursor()

    # Таблица пользователей
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL UNIQUE,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )''')

    # Таблица категорий
    c.execute('''CREATE TABLE IF NOT EXISTS categories (
                    category_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL
                )''')

    # Таблица товаров
    c.execute('''CREATE TABLE IF NOT EXISTS products (
                    product_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    description TEXT,
                    price REAL NOT NULL,
                    category_id INTEGER,
                    image_path TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (category_id) REFERENCES categories(category_id)
                )''')

    # Таблица заказов
    c.execute('''CREATE TABLE IF NOT EXISTS orders (
                    order_id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    total_amount REAL NOT NULL,
                    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    status TEXT DEFAULT 'pending',
                    FOREIGN KEY (user_id) REFERENCES users(user_id)
                )''')

    # Таблица элементов заказа
    c.execute('''CREATE TABLE IF NOT EXISTS order_items (
                    order_item_id INTEGER PRIMARY KEY,
                    order_id INTEGER,
                    product_id INTEGER,
                    quantity INTEGER NOT NULL,
                    price REAL NOT NULL,
                    FOREIGN KEY (order_id) REFERENCES orders(order_id),
                    FOREIGN KEY (product_id) REFERENCES products(product_id)
                )''')

    # Таблица отзывов
    c.execute('''CREATE TABLE IF NOT EXISTS reviews (
                    review_id INTEGER PRIMARY KEY,
                    product_id INTEGER,
                    user_id INTEGER,
                    rating INTEGER CHECK (rating >= 1 AND rating <= 5),
                    comment TEXT,
                    review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (product_id) REFERENCES products(product_id),
                    FOREIGN KEY (user_id) REFERENCES users(user_id)
                )''')

    conn.commit()
    conn.close()

# Функция для получения всех товаров
def get_all_products():
    conn = sqlite3.connect('sport_shop.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM products''')
    products = c.fetchall()
    conn.close()
    return products

# Функция для получения информации о конкретном товаре по ID
def get_product_by_id(product_id):
    conn = sqlite3.connect('sport_shop.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM products WHERE product_id=?''', (product_id,))
    product = c.fetchone()
    conn.close()
    return product

# Функция для добавления товара в базу данных
def add_product(name, description, price, category_id, image_path):
    conn = sqlite3.connect('sport_shop.db')
    c = conn.cursor()
    c.execute('''INSERT INTO products (name, description, price, category_id, image_path)
                 VALUES (?, ?, ?, ?, ?)''', (name, description, price, category_id, image_path))
    conn.commit()
    conn.close()

# Функция для обновления информации о товаре в базе данных
def update_product(name, description, price, category_id, image_path, product_id):
    conn = sqlite3.connect('sport_shop.db')
    c = conn.cursor()
    c.execute('''UPDATE products SET name=?, description=?, price=?, category_id=?, image_path=? WHERE product_id=?''',
              (name, description, price, category_id, image_path, product_id))
    conn.commit()
    conn.close()

# Функция для удаления товара из базы данных
def delete_product(product_id):
    conn = sqlite3.connect('sport_shop.db')
    c = conn.cursor()
    c.execute('''DELETE FROM products WHERE product_id=?''', (product_id,))
    conn.commit()
    conn.close()

# Создаем базу данных, если она еще не существует
create_database()
