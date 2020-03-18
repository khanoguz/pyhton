import os
menu = """
[1]Add new book
[2]Take a book
[3]Show all books
[Q]Quit
"""

book_list = [("Ruh adam","Atsız")]
def addnewbook(newbook:tuple,booklist:list):
    booklist.append(newbook)
    print("Book is added!")
    print("Press enter for menu")
    input()
def bookcontrol(book:tuple,booklist:list):
    if book in booklist:
        return True
    else:
        return False

def removebook(book:tuple,booklist:list):
    bookcontrol(book,booklist)
    if bookcontrol(book,booklist):
        booklist.remove(book)
        print("Book is removed")
        print("Press enter for menu")
        input()
    else:
        print("There is no a book with this name!")
        print("Press enter for menu")
        input()

def showbook(booklist:list):
    for i in booklist:
        print("""
        Book's Name:{} ------> Book's Writer:{}""".format(i[0],i[1]))
        



while True:
    os.system("clear")
    print(menu)
    a = input("Please choose:")
    
    if a == "1":
        book_name = input("Name of the book:")
        book_writer = input("Writer of the book:")
        new_book = (book_name,book_writer)
        addnewbook(new_book,book_list)
    
    elif a == "2":
        book_name = input("Write name of the book:")
        book_writer = input("Write writer name of the book:")
        book = (book_name,book_writer)
        removebook(book,book_list)
    
    elif a == "3":
        showbook(book_list)
        print("Press enter for menu")
        input()
    
    elif a == "q" or a == "Q":
        quit()

    
