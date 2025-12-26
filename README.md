# AbnaaEldawy - Product Management System

A web-based product management system built with Flask and SQL Server.

## Features

- 📦 Display all products
- 🔍 Search products by name
- ➕ Add new products
- ✏️ Edit product details
- 🗑️ Delete products
- 💰 Manage selling and purchase prices

## Prerequisites

- Python 3.x
- SQL Server
- ODBC Driver 18 for SQL Server

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/YOUR_USERNAME/AbnaaEldawy-main.git
cd AbnaaEldawy-main
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Setup the database:**
   - Open SQL Server Management Studio
   - Import the `products_db.sql` file
   - Update database connection settings in `app.py` (lines 8-11):
     ```python
     DB_SERVER = 'YOUR_SERVER_NAME'
     DB_NAME = 'products_db'
     DB_USER = 'YOUR_USERNAME'
     DB_PASSWORD = 'YOUR_PASSWORD'
     ```

## Usage

Run the application:
```bash
python app.py
```

Then open your browser and navigate to: `http://localhost:5000`

## Project Structure

```
AbnaaEldawy-main/
│
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── products_db.sql        # Database schema and data
├── templates/
│   └── index.html        # User interface
└── static/               # Static files (CSS, JS, Images)
```

## Technologies Used

- **Backend:** Flask (Python)
- **Database:** SQL Server
- **Frontend:** HTML, CSS, JavaScript

## API Endpoints

- `GET /api/products` - Get all products (with optional search parameter)
- `POST /api/products` - Add a new product
- `PUT /api/products/<id>` - Update a product
- `DELETE /api/products/<id>` - Delete a product

## License

MIT License

## Author

[Mohamed Hossam _ JUBA]
