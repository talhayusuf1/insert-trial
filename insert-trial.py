from re import T
import mysql.connector


def insertProduct(name, price, imageUrl, description):
    connection = mysql.connector.connect(
        host="localhost", user="root", password="Your Password", database="node-app")
    cursor = connection.cursor()
    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = (name, price, imageUrl, description)

    cursor.execute(sql, values)
    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayit eklendi")
        print(f" Son eklenen kayın id : {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata:", err)
    finally:
        connection.close()
        print("Database baglantısı kapandı.")


list = []
while True:
    name = input("urun adi: ")
    price = input("urun fiyatı: ")
    imageUrl = input("urun resim adi: ")
    description = input("urun aciklama: ")
    list.append((name, price, imageUrl, description))
    result = input("devam etmek istiyormusunuz? (e/h)")
    if result == "h":
        print("Kayıtlarınız Veritanbanına aktaarılıyor...")
        print(list)

# insertProduct(name, price, imageUrl, description)
