book = {
    "person1" : {
        "Name and Surname:" : "Oğuz Kağan Bilici",
        "Number" : "+905418648389",
        "Job:" : "engineer but poor",
        "Adress" : "Mustafa Kemal Paşa street",
        },
        "person2":{
            "Name and Surname" : "Adnan Bilici",
            "Number" : "+905053759289",
            "Job" : "Teacher",
            "Adress" : "Fatsa"
        }
    
}
while True:
    names = book.keys()
    a = input("Who is you wanna find:")
    if a in names:
        flag = True
    else:
        flag = False

    b = input("Information:")
    if flag:
        print(book.get(a,"Person isn't found!").get(b,"It cant be find"))
    else:
        print("there is not a person")