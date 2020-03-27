"""def amount(liste:list):
    a = 0
    for i in liste:
        a +=i
    return amount

and we can call this module in other py pages


#os module
import os

a = os.getcwd()

print(a)
print("path is changed")
os.chdir("/../")
a = os.getcwd()
print(a)

home_path = os.path.expanduser("~")
print(home_path)

print("files")

for i in os.listdir("."): #. means our rigth now path
    print(i)

import time

print("firt line")
time.sleep(5) #delay
print("second line")

time1 = time.time()
time.sleep(2)
time2 = time.time()

print("substraction: {}".format(time2-time1))

import random #it doenst work on pycharm idk why
rand = random.randint(1,10)

print(rand)

"""