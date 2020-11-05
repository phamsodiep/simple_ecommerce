import sqlite3
import os
import sys
import urllib.request
from PIL import Image
import io


if len(sys.argv) < 2:
    cmd = "{0} <product id>"
    print(cmd.format(sys.argv[0]))
    print("Where:")
    legend = "".join([
        "\t<product id>: id of target product need deleting",
    ])
    print(legend)
    sys.exit()

DB_FILE_NAME = "simple-e-commerce.db"
connection = sqlite3.connect(DB_FILE_NAME)



sql = "".join([
    "DELETE ",
    "FROM products ",
    "WHERE id = ",
    sys.argv[1]
])
print (sql)
cursor = connection.execute(sql)

connection.commit()

print("Operation done successfully")
connection.close()