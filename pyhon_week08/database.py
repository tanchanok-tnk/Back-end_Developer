import mysql.connector as mysqlcon
mydb = mysqlcon.connect(
    host = "localhost",
    user = "root",
    password ="0630608821",
    database = "online store"
)
print(mydb)
