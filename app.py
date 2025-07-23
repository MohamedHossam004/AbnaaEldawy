import os
from flask import Flask, render_template, request, jsonify
import pyodbc

app = Flask(__name__)

# إعداد الاتصال بقاعدة بيانات SQL Server
DB_SERVER = 'DESKTOP-A6E1M73'  # عدلها إذا كان السيرفر مختلف
DB_NAME = 'products_db'  # اسم قاعدة البيانات
DB_USER = 'sa'           # اسم المستخدم
DB_PASSWORD = '23122312'  # كلمة المرور

conn_str = (
    'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=DESKTOP-A6E1M73;'
    'DATABASE=products_db;'
    'UID=sa;'
    'PWD=23122312;'
    'TrustServerCertificate=yes;'
)

def get_db_connection():
    return pyodbc.connect(conn_str)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/products', methods=['GET'])
def search_products():
    search = request.args.get('search', '')
    conn = get_db_connection()
    cursor = conn.cursor()
    if search:
        query = """
            SELECT ID, Product_Name, Selling_Price, Purchase_Price
            FROM products
            WHERE Product_Name LIKE ?
            ORDER BY Product_Name
        """
        cursor.execute(query, f'%{search}%')
    else:
        query = "SELECT ID, Product_Name, Selling_Price, Purchase_Price FROM products ORDER BY Product_Name"
        cursor.execute(query)
    rows = cursor.fetchall()
    products = [
        {
            'id': row[0],
            'name': row[1],
            'selling_price': row[2],
            'purchase_price': row[3]
        } for row in rows
    ]
    conn.close()
    return jsonify(products)

@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    if not data:
        return jsonify({'status': 'error', 'message': 'No data provided'}), 400
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        UPDATE products
        SET Product_Name=?, Selling_Price=?, Purchase_Price=?
        WHERE ID=?
    """
    cursor.execute(query, data['name'], data['selling_price'], data['purchase_price'], product_id)
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'})

@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM products WHERE ID=?"
    cursor.execute(query, product_id)
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'})

@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.json
    if not data or not all(k in data for k in ('name', 'selling_price', 'purchase_price')):
        return jsonify({'status': 'error', 'message': 'بيانات غير مكتملة'}), 400
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO products (Product_Name, Selling_Price, Purchase_Price, Discount)
        VALUES (?, ?, ?, 0)
    """
    cursor.execute(query, data['name'], data['selling_price'], data['purchase_price'])
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True) 