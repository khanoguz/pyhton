menu ="""##########
\tWelcome
Please choose what you wanna do:
[1]Add new book
[2]Show all books
[3]Quit
##########
"""
booklist = ["Ruh Adam","Bozkurtlar Diriliyor","Deli Kurt","Türkçülüğün Esasları"]

def addnewbook(bookname,list):
    print("Enter the name of the book: {}".format(bookname))
    list+=[bookname]

def showallbooks(list):
    for i in list:
        print("Name of the book:{}".format(i))
def quit():
    quit()

while True:
    print(menu)
    inputs =input("Your choose:")

    if inputs == "1":
        bookname = input("Book name:")
        addnewbook(bookname,booklist)
    elif inputs =="2":
        showallbooks(booklist)
    elif inputs =="3":
        quit()
