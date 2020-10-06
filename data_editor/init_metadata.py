import sqlite3
import os


DB_FILE_NAME = "simple-e-commerce.db"
connection = sqlite3.connect(DB_FILE_NAME)
cursor = connection.cursor()



#             0   1           2         3            4           5      6
# comboItems=["", "Có/Không", "Khoảng", "Tham khảo", "Danh mục", "Chữ", "Chiều"]


characteristics = [
    [
        1,
        "kích cỡ",
        "Khoảng",
        "0, 10, tấc",
    ],
    [
        2,
        "thể tích hồ tối thiểu",
        "Chiều",
        "1 lít",
    ],
    [
        3,
        "độ khó chăm sóc",
        "Danh mục",
        "2",
    ],
    [
        4,
        "tính cách",
        "Danh mục",
        "3",
    ],
    [
        5,
        "nhiệt độ nước",
        "Khoảng",
        "10, 50, °C",
    ],
    [
        6,
        "pH nước",
        "Khoảng",
        "-7, 7, pH",
    ],
    [
        7,
        "kích cỡ tối đa",
        "Chiều",
        "1 tấc",
    ],
    [
        8,
        "màu sắc",
        "Danh mục",
        "1",
    ],
    [
        9,
        "loại thức ăn",
        "Danh mục",
        "4n",
    ],
    [
        10,
        "thức ăn chính",
        "Tham khảo",
        "",
    ],
    [
        11,
        "xuất xứ",
        "Danh mục",
        "5",
    ],
    [
        12,
        "họ",
        "Chữ",
        "",
    ],
    [
        13,
        "tuổi thọ",
        "Khoảng",
        "1, 120, tháng",
    ],
    [
        14,
        "hành phong thủy",
        "Danh mục",
        "7",
    ],
    [
        15,
        "kích cỡ",
        "Khoảng",
        "0, 100, cm",
    ],
    [
        16,
        "yêu cầu CO2",
        "Danh mục",
        "6",
    ]
]


COMBO_ITEMS = ["", "Có/Không", "Khoảng", "Tham khảo", "Danh mục", "Chữ", "Chiều"]
for data in characteristics:
    typeStr = [i for i in range(0, len(COMBO_ITEMS)) if COMBO_ITEMS[i] == data[2]]
    cursor.execute("""
        INSERT INTO characteristics (id, name, type, definition)
        VALUES ({0}, '{1}', {2}, '{3}')
    """.format(data[0], data[1], typeStr[0], data[3]))


# "5_Thuốc và hóa chất" "6_Hồ - đèn - bơm - lọc" "7_Dụng cụ" "8_Trang trí" "9_Linh tinh"
CAT_CHARS = [
# 0
    [],
# 1_Cá
    list(range(1, 15)),
# 2_Cây thủy sinh
    [3, 15],
# 3_Động vật khác
    [],
# 4_Thức ăn
    [],
]
for i in range(0, len(CAT_CHARS)):
    for j in range(0, len(CAT_CHARS[i])):
        charId = CAT_CHARS[i][j]
        cursor.execute("""
            INSERT INTO cat_char (catId, charId)
            VALUES ({0}, {1})
        """.format(i, charId))


connection.commit()

