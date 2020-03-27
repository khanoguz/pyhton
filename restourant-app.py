import os

tables = dict()

for i in range(1,10):
    tables[i] = 0


def records(file_name):
    try:
        file = open(file_name)
        datas = file.read()
        datas = datas.split("\n")
        datas.pop()
        file.close()
        flag = True

    except FileNotFoundError:
        file = open(file_name,"w")  
        file.close()
        flag = False

    if flag:
        for i in enumerate(datas):
            tables[i[1]] = float(i[1])
    else:
        pass        
        

def add():
    tableNo = int(input("Table No:"))
    try:
        fee = tables[tableNo]
        addfee = float(input("Pay:"))
        amount = fee + addfee
        tables[tableNo] = amount
    except KeyError:
        print("Please choose right table!")
   

def delete():   
    tableNo = int(input("Table No:"))
    try:
        fee = tables[tableNo]
        deletefee = float(input("Pay:"))
        amount = fee - deletefee
        tables[tableNo] = amount

    except KeyError:
        print("Please choose right table!")

def main():
    records("kayitlar.txt")
    while True:
        os.system("clear")
        print("""
    [1]Show the tables
    [2]Add new cheque
    [3]Delete cheque
    [Q]Quit
    """
        )
    
        secim = input("What do you want to do:")
    
        if secim == "1":
            for i in range(1,10):
                    print("Table {} is cheque {}".format(i,tables[i]))
            print("It's done,press enter for main menu!")
            input()

        elif secim == "2":
            add()
            print("It's done,press enter for main menu!")
            input()

        elif secim == "3":
            delete()
            print("It's done,press enter for main menu!")
            input()

        elif secim == "Q" or secim == "q":
            quit()


    
main()
