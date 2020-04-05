import sqlite3

books = [
("Nihat Atsız","Bozkurtlar"),
("Ziya Gökalp","Türkçülüğün Esasları"),
("Yusuf Akçura","Üç Tarzı Siyaset")
]

db = sqlite3.connect("books.db") #open or create

cursor = db.cursor() #create for cursor

"""
cursor.execute("CREATE TABLE IF NOT EXISTS books (writer,books)")
for datas in books:
    cursor.execute("INSERT INTO books VALUES (?,?)",datas)
db.commit()

cursor.execute("SELECT * FROM books")

datas = cursor.fetchall()#show all datas"


for i in books:
    print(cursor.fetchone())
print(cursor.fetchone()) # show just one data
print(cursor.fetchone())


datas = cursor.fetchmany(2) #different way to see datas

for i in datas:
    print(i)
    
    """
cursor.execute("SELECT * FROM books WHERE writer = 'Nihal Atsız'")

data = cursor.fetchall()

for i in data:
    print(i)

db.close()

