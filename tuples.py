#tuple = ("adasdasd",)
#almost same with lists.
#but you can not add or delete something in tuple
#tuples faster than lists.

tuplee = tuple()

for i in dir(tuple()):
    if "__" not in i:
        print(i)

# just you can count and index
