import random
print('โปรแกรมเป่ายิงฉุบ')
while True:
    a = random.choice(["ค้อน","กรรไกร","กระดาษ"])
    print(a)
    b = str(input("ระบุ : "))
    if b == a :
        print("เสมอ")
    elif a == "กรรไกร" and b == "ค้อน" :
        print("คุณชนะ")
    elif a == "ค้อน" and b == "กระดาษ" :
        print("คุณชนะ")
    elif a == "กระดาษ" and b == "กรรไกร" :
        print("คุณชนะ")
    else :
        print("คุณแพ้")
    