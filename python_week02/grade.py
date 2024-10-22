print("ตรวจผลการสอบ")
a=int(input("กรุณากรอกคะแนน"))
if a < 0 or a > 100 :
    print("ใส่เลข 0 - 100")
elif a >= 80 :
    print("เกรด 4 ")
elif a >= 70 :
    print("เกรด 3")
elif a >=  60:
    print("เกรด 2")
elif a >= 50 :
    print("เกรด 1")
elif a <= 49 :
    print("เกรด 0")
