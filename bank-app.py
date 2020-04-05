import os

class Customer():
    def __init__(self,ID,PASSPORT,NAME):
        self.ID = ID
        self.passport = PASSPORT
        self.name = NAME
        self.remainder = 0




class Bank():
    def __init__(self):
        self.customers = list()

    def addcustomer(self,ID,PASSPORT,NAME):
            self.customers.append(Customer(ID,PASSPORT,NAME))
            print("Thank you for register in our bank")

def main():
    bank = Bank()
    while True:
        print("""
        [1]Bank Customer
        [2]Foreign Customer
              """)
        sec = input(":")

        if sec == "1":
            os.system("clear")
            ids = [i.id for i in bank.customers]
            ID = input("ID:")
            if ID in ids:
                for customer in bank.customers():
                    if ID == customer.ID:
                        passport = input("passport:")
                        if passport == customer.passport:
                            print("wait...")
                            while True:
                                os.system("clear")
                                print("welcome {}".format(customer.name))
                                print("""
                                [1]check ur account
                                [2]add money to your remainder
                                [3]add money to else remainder
                                [4]get money
                                [5]Quit
                                """)
                                sec2 = input(":")
                                os.system("clear")
                                if sec2 == "1":
                                    print("your remainder: {}".format(customer.remainder))
                                    input("enter for main")
                                elif sec2 == "2":
                                    amount = int(input("Amount:"))
                                    check = input("add {} money to your remainder:".format(amount))
                                    if check == "e" or "E":
                                        customer.remainder += amount
                                        print("wait..")
                                        input("enter for main")
                                    elif check == "h" or "H":
                                        input("enter for main")
                                    else:
                                        print("wrong button")
                                        input("enter for main")

                                elif sec2 == "3":
                                    idd = input("ID for add money:")
                                    if idd in ids:
                                        for i in bank.customers:
                                            if idd == i.id:
                                                print("ID is correct")
                                                if amount <= customer.remainder:
                                                    check2 = input("Do u confirm that Name: {} ----> Amount: {}".format(customer.name,customer.remainder))
                                                    if check2 == "e" or "E":
                                                        i.remainder += amount
                                                        customer.remainder -= amount
                                                    elif check2 == "h" or "H":
                                                        input("enter for main")
                                                    else:
                                                        print("wrong button")
                                                        input("enter for main")
                                                else:
                                                    print("Not enough remainder for do this")

                                            else:
                                                print("customer is not found")
                                                input("enter for main")

                                elif sec2 == "4":
                                    take = int(input("amount money to take:"))
                                    if take <= customer.remainder:
                                        check3 = input("do u confirm this:")
                                        if check3 == "e" or "E":
                                            customer.remainder -= take
                                            input("enter for main")
                                        elif check3 == "h" or "H":
                                            input("enter for main")
                                        else:
                                            print("wrong button")
                                            input("enter for main")
                                    else:
                                        print("not enough remainder")
                                        input("enter for main")

                                elif sec2 == "q" or "Q":
                                    input("enter for main")


        if sec == "2":
            ID = input("ID:")
            Name = input("Name:")
            Pasport = input("Pasport:")
            Bank.addcustomer(ID,Pasport,Name)






















if __name__ == '__main__':
    main()



