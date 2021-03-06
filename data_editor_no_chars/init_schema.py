import sqlite3
import os


DB_FILE_NAME = "simple-e-commerce.db"
if os.path.exists(DB_FILE_NAME):
    os.remove(DB_FILE_NAME)
connection = sqlite3.connect(DB_FILE_NAME)
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE products
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        catId INTEGER,
        priority INTEGER,
        name TEXT,
        priceMin INTEGER,
        priceMax INTEGER,
        imgUrl TEXT,
        activeImg INTEGER,
        briefImgScale INTEGER,
        briefImgCroppedX INTEGER,
        briefImgCroppedY INTEGER,
        desc TEXT,
        briefImgUrl TEXT
    )
""")

connection.commit()

