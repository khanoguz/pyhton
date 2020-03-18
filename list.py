#booklist = [] or booklist = list()

booklist = ["Ruh Adam","Bozkurtlar Diriliyor","Deli Kurt","Türkçülüğün Esasları",["Dokuz Işık","Osmancık","Üç Tarz-ı Siyaset","Kilit"]]
def listele(list):
    for i in list:
        print("name of the book: {}".format(i))

print(booklist[0])
print(booklist[-1][3])

booklist.append("Bozkurt")
booklist.append("Simyacı")
booklist.append("Amak-ı Hayal")
listele(booklist)
print(25*'-')
print(booklist.count("Bozkurt"))
print(25*'-')
new_book_list = booklist.copy()
booklist.remove("Amak-ı Hayal")
booklist.remove("Simyacı")
print(new_book_list)
print(booklist)
print(25*'-')
new_book_list.extend(booklist)
print(new_book_list)
print(25*'-')
sira = booklist.index("Deli Kurt")
print(sira)
print(25*'-')
#booklist.sort() -> sorting


