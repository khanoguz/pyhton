print("""
[1]Toplama
[2]Cikarma
[3]Carpma
[4]Bolme
[Q]Cikis
""")


m = input("Lutfen yapmak istediginiz islemi seciniz:")

print("==================================")
if m == "1":
    x = input("ilk sayiyi giriniz:")
    x = float(x)
    y = input("ikinci sayiyi giriniz:")
    y = float(y)
    print("islem sonucu:",x+y)
elif m == "2":
    x = float(input("ilk sayiyi giriniz:"))
    y = float(input("ikinci sayiyi giriniz:"))
    print("islem sonucu:",x-y)
elif m == "3":
    x = float(input("ilk sayiyi giriniz:"))
    y = float(input("ikinci sayiyi giriniz:"))
    print("islem sonucu",x*y)
elif m == "4":
    x = float(input("ilk sayiyi giriniz:"))
    y = float(input("ikinci sayiyi giriniz:"))
    print("islem sonucu",x/y)
elif m == 'q' or m == 'Q':
    print("cikis yaptiniz")
    exit()
print("==================================")



    









