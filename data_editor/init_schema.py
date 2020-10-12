import sqlite3
import os


DB_FILE_NAME = "simple-e-commerce.db"
if os.path.exists(DB_FILE_NAME):
    os.remove(DB_FILE_NAME)
connection = sqlite3.connect(DB_FILE_NAME)
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE characteristics
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        type INTEGER,
        definition TEXT
    )
""")

cursor.execute("""
    CREATE TABLE cat_char
    (
        catId INTEGER,
        charId INTEGER,
        PRIMARY KEY (catId, charId),
        FOREIGN KEY (charId) REFERENCES characteristics(id)
    )
""")

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
        desc TEXT
    )
""")

cursor.execute("""
    CREATE TABLE prod_char
    (
        proId INTEGER,
        charId INTEGER,
        value TEXT,
        PRIMARY KEY (proId, charId),
        FOREIGN KEY (proId) REFERENCES products(id),
        FOREIGN KEY (charId) REFERENCES characteristics(id)
    )
""")

connection.commit()

