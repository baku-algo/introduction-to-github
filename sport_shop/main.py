from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Helper function to get all products
def get_all_products():
    # Заглушка. Добавьте логику для работы с базой данных.
    return []

# Helper function to get a product by ID
def get_product_by_id(product_id):
    # Заглушка. Добавьте логику для работы с базой данных.
    return None

# Helper function to add a product
def add_product(name, description, price, quantity, image_path):
    # Заглушка. Добавьте логику для работы с базой данных.
    pass

# Helper function to update a product
def update_product(name, description, price, quantity, image_path, product_id):
    # Заглушка. Добавьте логику для работы с базой данных.
    pass

# Helper function to delete a product
def delete_product(product_id):
    # Заглушка. Добавьте логику для работы с базой данных.
    pass

@app.route('/')
def index():
    products = get_all_products()
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = get_product_by_id(product_id)
    if product:
        return render_template('product_detail.html', product=product)
    else:
        return "Product not found", 404

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        # Исправлено: request.form возвращает словарь, к ключам нужно обращаться через []
        product_id = request.form.get('product_id')  # Исправлено с request.form('product_id')
        name = request.form.get('name')  # Исправлено с request.form('name')
        description = request.form.get('description')  # Исправлено с request.form('description')
        price = request.form.get('price')  # Исправлено с request.form('price')
        quantity = request.form.get('quantity')  # Исправлено с request.form('quantity')
        image_path = request.form.get('image_path')  # Исправлено с request.form('image_path')
        action = request.form.get('action')  # Исправлено с request.form('action')

        if action == 'add':
            add_product(name, description, price, quantity, image_path)
        elif action == 'edit' and product_id:
            update_product(name, description, price, quantity, image_path, product_id)
        elif action == 'delete' and product_id:
            delete_product(product_id)

        return redirect(url_for('admin'))

    products = get_all_products()
    return render_template('admin.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
