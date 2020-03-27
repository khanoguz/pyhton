#5! = 5x4x3x2x1

def fact(number):
    if number == 1:
        return 1
    else:
        return number * fact(number-1)


print(fact(5))