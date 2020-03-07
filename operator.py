"""
print("------------------------")
print("ARITMETIK OPERATORLER")
print("str toplama:","oguz"+"kagan")
print("str ile int carpma:",3*" oguz kagan")
print("kuvvet alma:",5**3)
print("normal bolme:",5/2)
print("taban bolme",5//2)
print("------------------------")
print("------------------------")

print("KARSILASTIRMA OPERATORLERI")
giris = input("Parola:")
sifre = "deneme"

if giris == sifre:
    print("giris basarili")
elif giris != sifre:
    print("giris basarisiz")

print("----")

giriss = int(input("sayi giriniz:"))

if giriss <= 50:
    print("sayi 50'den kucuktur veya 50'ye esittir")
elif giriss > 50:
    print("sayi 50'den buyuktur")

print("------------------------")
print("------------------------")

print("BOOL OPERATOR")
sayi = int(input("sayi giriniz:"))

if sayi >2 and sayi <5:
    print("sayi 2 ve 5 arasindadir")

elif sayi> 5 or sayi <2:
    print("sayi 5'ten buyuk veya 2'denn kucuktur")

x = input("x'i giriniz:")

if not bool(x):
    print("true")
else:
    print("false")


print("------------------------")
print("------------------------")

print("AITLIK OPERATORU")


parola = input("parola giriniz:")
if "_" not in parola:
    print("lutfen parolanizda '_' kullanınız")
else:
    print("basarili")

print("------------------------")
print("------------------------")
"""
