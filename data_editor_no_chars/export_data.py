import sqlite3
import os
import urllib.request
from PIL import Image
import io


DB_FILE_NAME = "simple-e-commerce.db"
connection = sqlite3.connect(DB_FILE_NAME)

#oFile = open("clip.txt", "w")
oFile = io.open("clip.json", "w", encoding="utf-8")

DATA = """{
  "productCategories": [
    {
      "id": 0,
      "name": "Sản phẩm"
    },
    {
      "id": 1,
      "name": "Cá",
      "hasProducts": true,
      "children": [
        {
          "id": 11,
          "name": "Cá chép",
          "children": [
          ]
        },
        {
          "id": 12,
          "name": "Cá Betta",
          "children": [
          ]
        },
        {
          "id": 13,
          "name": "Cá rồng",
          "children": [
          ]
        },
        {
          "id": 14,
          "name": "Cá khác",
          "children": [
          ]
        }
      ]
    },
    {
      "id": 2,
      "name": "Thủy sinh",
      "children": [
        {
          "id": 21,
          "name": "Cây thủy sinh",
          "children": [
          ]
        },
        {
          "id": 22,
          "name": "Đèn thủy sinh",
          "children": [
          ]
        },
        {
          "id": 23,
          "name": "Các thứ khác",
          "children": [
          ]
        }
      ]
    },
    {
      "id": 3,
      "name": "Động vật khác",
      "children": [
      ]
    },
    {
      "id": 4,
      "name": "Thức ăn",
      "children": [
      ]
    },
    {
      "id": 5,
      "name": "Hồ",
      "children": [
        {
          "id": 51,
          "name": "Hồ cá kiểng",
          "children": [
          ]
        },
        {
          "id": 52,
          "name": "Hồ thủy sinh",
          "children": [
          ]
        }
      ]
    },
    {
      "id": 6,
      "name": "Dụng cụ",
      "children": [
        {
          "id": 61,
          "name": "Đèn cá kiểng",
          "children": [
          ]
        },
        {
          "id": 62,
          "name": "Bơm lọc",
          "children": [
          ]
        },
        {
          "id": 63,
          "name": "Dụng cụ khác",
          "children": [
          ]
        }
      ]
    },
    {
      "id": 7,
      "name": "Linh tinh",
      "children": [
        {
          "id": 71,
          "name": "Trang trí",
          "children": [
          ]
        },
        {
          "id": 72,
          "name": "Thuốc và hóa chất",
          "children": [
          ]
        }
      ]
    },

    {
      "id": 0,
      "name": "Bài viết"
    },
    {
      "id": 100,
      "name": "Hướng dẫn setup",
      "children": [
      ]
    },
    {
      "id": 200,
      "name": "Mẹo",
      "children": [
        {
          "id": 2001,
          "name": "Mẹo chăm sóc",
          "children": [
          ]
        },
        {
          "id": 2002,
          "name": "Mẹo phong thủy",
          "children": [
          ]
        }
      ]
    }
  ],

  "products": {
"""

oFile.write(DATA)

cursor = connection.execute("".join([
    "SELECT DISTINCT ",
        "catId ",
    "FROM products"
]))

# retrive all catId
catIds = []
for row in cursor:
    catIds.append(row[0])

productCount = 0
productMaps = {}
# retrieve all product id for each catId
for catId in catIds:
    productMaps[catId] = []
    cursor = connection.execute("".join([
        "SELECT id ",
        "FROM products ",
        "WHERE catId = ",
        str(catId)
    ]))
    for row in cursor:
        pId = row[0]
        productMaps[catId].append(pId)
        productCount += 1

# print category -> products map
catCounter = len(productMaps.keys())
for catId in productMaps:
    catCounter -= 1
    catSep = "," if catCounter > 0 else ""
    products = productMaps[catId]
    oFile.write("    \"" + str(catId) + "\": [")
    productCounter = len(products)
    for productId in products:
        productCounter -= 1
        productSep = ", " if productCounter > 0 else ""
        oFile.write(str(productId) + productSep)
    oFile.write("]" + catSep + "\n")
oFile.write("  },\n")


# print product id -> product map
oFile.write("\n  \"product\": {\n")
cursor = connection.execute("".join([
    "SELECT id, name, priceMin, priceMax, imgUrl, desc, briefImgUrl ",
    "FROM products"
]))

productCounter = productCount
for row in cursor:
    productCounter -= 1
    productSep = "," if productCounter > 0 else ""
    pId = row[0]
    name = row[1]
    priceMin = row[2]
    priceMax = row[3]
    imgUrl = row[4]
    desc = row[5]
    briefImgUrl = row[6]
    oFile.write("    \"" + str(pId) + "\": {\n")
    # name
    oFile.write("      \"name\": \"" + str(name) + "\",\n")
    oFile.write("      \"priceMin\": " + str(priceMin) + ",\n")
    oFile.write("      \"priceMax\": " + str(priceMax) + ",\n")
    oFile.write("      \"imgUrl\": \"" + str(imgUrl) + "\",\n")
    desc = str(desc).replace("\"", "\\\"")
    oFile.write("      \"desc\": \"" + str(desc) + "\",\n")
    oFile.write("      \"briefImgUrl\": \"" + str(briefImgUrl) + "\"\n")
    oFile.write("    }" + productSep + "\n")

oFile.write("  }\n")



oFile.write("}\n")
oFile.close()
