nomre_1=int(input("Enter First Score: "))
nomre_2=int(input("Enter 2nd Score: "))
nomre_3=int(input("Enter 3rd Score: "))

moadel=(nomre_1+nomre_2+nomre_3)/3
shahriye=1000

if moadel<10:
    print("مردود")
    print("Jarime: ", shahriye*2)
    print("shahriye: ",shahriye)
    print("Your tuition fee is :", (shahriye*3))

if 10<moadel<12:
    print("قبول")
    print("Jarime: 500")
    print("shahriye: ",shahriye)
    print("Your tuition fee is :", (shahriye+500))

if 12<moadel<16:
    print("قبول خوب")
    print("Your tuition fee is :", shahriye)

if 16<moadel<18:
    print("قبول عالی")
    print("Discount: ",shahriye * 0.7)
    print("shahriye: ",shahriye)
    print("Your tuition fee is :", (shahriye-shahriye * 0.7))

if 18<moadel<20:
    print("قبول ممتاز")
    print("Discount: ",shahriye * 0.3)
    print("shahriye: ",shahriye)
    print("Your tuition fee is :", (shahriye - shahriye * 0.3))
