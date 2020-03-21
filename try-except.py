dividend = float(input("Divindend: "))
divider = float(input("Divider:"))

try:
    print("Result:", dividend/divider)
except ZeroDivisionError as error:
    print("Divide to 0 is undefined")
    print("Error is:")
    print(error)

except TypeError:
    (print("Data is not supporting"))

    
finally:
    print("It works all cases")  


#raise
#number = int(input("Number:"))

#if numbber == 5:
    #raise Exception("you cant access 5")
