import sqlite3
import os
import urllib.request
from PIL import Image
import io


DB_FILE_NAME = "simple-e-commerce.db"
connection = sqlite3.connect(DB_FILE_NAME)


def extractFileName(url):
    lastIdx = 0
    try:
        lastIdx = url.rindex('/')
    except:
        return None
    return url[lastIdx + 1:len(url)]


cursor = connection.execute("".join([
    "SELECT ",
        "id, imgUrl, briefImgScale, briefImgCroppedX, briefImgCroppedY ",
    "FROM products"
]))

for row in cursor:
    id = row[0]
    srcUrl = row[1]
    scaleLevel = row[2]
    briefImgCroppedX = row[3]
    briefImgCroppedY = row[4]
    print(id)
    print(srcUrl)
    print(extractFileName(srcUrl))
    print(scaleLevel) # image scale 0:100%  1:50%  2:25%  3:12.5%
    response = urllib.request.urlopen(srcUrl)
    data = response.read()
    image = Image.open(io.BytesIO(data))
    div = 1
    # if scaleLevel == 1:
        # width, height = image.size
        # width = width // 2
        # height = height // 2
        # size = width, height
        # image.thumbnail(size, Image.ANTIALIAS)
    # elif scaleLevel == 2:
        # width, height = image.size
        # width = width // 4
        # height = height // 4
        # size = width, height
        # image.thumbnail(size, Image.ANTIALIAS)
    # elif scaleLevel == 3:
        # width, height = image.size
        # width = width // 8
        # height = height // 8
        # size = width, height
        # image.thumbnail(size, Image.ANTIALIAS)

    if scaleLevel == 1:
        div = 2
    elif scaleLevel == 2:
        div = 4
    elif scaleLevel == 3:
        div = 8

    if div > 1:
        width, height = image.size
        width = width // div
        height = height // div
        size = width, height
        image.thumbnail(size, Image.ANTIALIAS)

    if scaleLevel == 3:
        briefImgCroppedX = 0
        briefImgCroppedY = 0

    # 1800 // 8 = 225
    # 1200 // 8 = 150
    cropImg = image.crop((briefImgCroppedX, briefImgCroppedY, briefImgCroppedX + 225, briefImgCroppedY + 150))
    try:
        cropImg.save(extractFileName(srcUrl))
    except:
        pass
    #image.show()
    print("")
