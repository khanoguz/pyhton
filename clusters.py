#cluster = set()

a = set([1,2,3,4,5,6,7])
print(a)
b = set([4,5,6,7,8,9,10])
print(b)


print(25*"-")

a.add(7)
print(a)
print(25*"-")
a.discard(1)
print(a)
print(25*"-")
a.remove(3) #if there is no 3, you get error message
print(a)
print(25*"-")
print(a.difference(b))
print(25*'-')
b.difference_update(a)
print(b)
print(25*'-')
a = set([1,2,3,4,5,6,7])
b = set([4,5,6,7,8,9,10])
print(a.intersection(b))





