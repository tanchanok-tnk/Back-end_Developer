import database
mycursor = database.mydb.cursor() #เก็บการทำงานของmysql
sql = "INSERT INTO subject VALUES (%s,%s)"
val = ('6','test')
mycursor.execute(sql,val)
#mycursor.execute("INSERT INTO subject VALUES ('6','test')")
database.mydb.commit() #ยืนยันการเปลี่ยนแปลง
