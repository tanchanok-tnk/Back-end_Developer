import database
mycursor = database.mydb.cursor() #เก็บการทำงานของsql

def show_table():
    mycursor.execute("SHOW TABLES")
    table = mycursor.fetchall() #ทำให้แสดงผล
    print('หัวข้อทั้งหมด') #เอามาแสดงผล
    for i in table:
        print(i)

#users
def select_users():
    name = input('ใส่userที่ต้องการค้นหา : ')
    mycursor.execute(f"SELECT * FROM users where username like '%{name}%'")
    myresulf = mycursor.fetchall()
    for i in myresulf:
        print(i)

#products
def select_products():
    name = input('ใส่productที่ต้องการค้นหา : ')
    mycursor.execute(f"SELECT * FROM products where product_name like '%{name}%'")
    myresulf = mycursor.fetchall()
    for i in myresulf:
        print(i)

#categories
def select_categories():
    name = input('ใส่categoriesที่ต้องการค้นหา : ')
    mycursor.execute(f"SELECT * FROM categories where category_name like '%{name}%'")
    myresulf = mycursor.fetchall()
    for i in myresulf:
        print(i)

#orders
def select_orders():
    name = input('ใส่orderที่ต้องการค้นหา : ')
    mycursor.execute(f"SELECT * FROM orders where user_id like '%{name}%'")
    myresulf = mycursor.fetchall()
    for i in myresulf:
        print(i)

def start():
    while True:
        print("\nเมนูหลัก:")
        user_input = input("กรุณาพิมพ์คำว่า 'users', 'product', 'categories', 'order' หรือ 'close' เพื่อจบการทำงานทั้งหมด: ")

        if user_input == "user":
            select_users() # ไปที่ผู้ใช้งาน
        elif user_input == "product":
            select_products()  # ไปที่สินค้า
        elif user_input == "categories":
            select_categories()  # ไปที่หมวดหมู่
        elif user_input == "order":
            select_orders()  # ไปที่order
        elif user_input == "close":
            print("ขอบคุณที่เข้ามาเล่นจ้า")
            break  # ออกจากโปรแกรม
        else:
            print("กรุณาพิมพ์คำสั่งที่ถูกต้อง เช่น 'user', 'product', 'categories', 'order' หรือ 'close'")

start()