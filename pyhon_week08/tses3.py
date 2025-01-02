import database
import datetime
mycursor = database.mydb.cursor()

def insert_categories():
    a = int(input("category_id : "))
    b = str(input("category_name : "))
    val = (a, b)
    sql = "INSERT INTO categories VALUES (%s , %s)"
    mycursor.execute(sql,val) 
    
    database.mydb.commit()

def insert_users():
    a = int(input("user_id : "))
    b = str(input("username : "))
    c = str(input("password : "))
    d = str(input("email : "))
    e = str(input("user_role = admin,customer : "))
    val = (a, b ,c ,d ,e)
    sql = "INSERT INTO users VALUES (%s , %s , %s , %s , %s)"
    mycursor.execute(sql,val) 

    database.mydb.commit()

def insert_orders():
    b = str(input("user_id : "))
    c = datetime.datetime.today()
    print (c.strftime("%d/%m/%y %H:%M:%S"))
    d = float(input("total_amount : "))
    e = str(input("status(รอดําเนินการ,กำลังจัดส่ง,จัดส่งสําเร็จ,ยกเลิกรายการ) : "))
    f = str(input("product_id : "))
    sql = "INSERT INTO orders VALUES (%s , %s , %s , %s , %s , %s)"
    a = int(input("order_id : "))
    val = (a, b ,c ,d ,e ,f)
    mycursor.execute(sql,val) 

    database.mydb.commit()

def insert_products(): 
    a = int(input("product_id : "))
    b = str(input("product_name : "))
    c = str(input("description : "))
    d = float(input("price : "))
    e = int(input("stock : "))
    f = int(input("category_id : "))
    val = (a, b ,c ,d ,e ,f)
    sql = "INSERT INTO products VALUES (%s , %s , %s , %s , %s , %s)"
    mycursor.execute(sql,val) 

    database.mydb.commit()

insert_products()