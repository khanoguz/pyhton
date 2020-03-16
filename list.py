#booklist = [] or booklist = list()

booklist = ["Ruh Adam","Bozkurtlar Diriliyor","Deli Kurt","Türkçülüğün Esasları"]

new_book = input("please enter new book:")
booklist+=[new_book]

for i in booklist:
    print("name of the book: {}".format(i))