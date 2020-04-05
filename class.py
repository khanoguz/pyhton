"""class Soldier():  #name of the class starts with big
    health = 100
    name = 'Oğuz Kağan'
    weapon = 'Pistol'


print(Soldier.health)

Soldier.bullet = 50 #we can add new things

print(Soldier.bullet)



class Order():
    company = []
    amount = ''
    date = ''

gum = Order()
book = Order()
gum.company += ['Ülker']
gum.amount = 1000
gum.date = "28.03.2020"


book.company += ['Ötüken Yayınları']
book.amount = 10000
gum.date = "28.03.2020"

print(gum.company,":",gum.amount,"amount",gum.date)
print(book.company,":",book.amount,"amount",gum.date)

"""

class Soldier():
    def __init__(self,name,power):
        self.ability = []
        self.name = name
        self.power = power
        self.ability = []

oğuz = Soldier("Oğuz",99)
kağan = Soldier("Kağan",100)
oğuz.ability += ['Warrior']
kağan.ability += ['Fighter']

print(oğuz.name)
print(oğuz.power)
print(oğuz.ability)


print("----")
print(kağan.name)
print(kağan.power)
print(kağan.ability)

