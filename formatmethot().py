name = "oğuz kağan"
surname = "bilici"
age = 22
salary = 9999999999999999
format1 = "{ad} {soyad}".format(ad=name, soyad=surname)
format2 = "{1} {0}".format(name,surname)
format3 = "|{:>20}|".format(name)
format4 = "/{:<20}\\".format(surname)
format5 = "|{:^30}|".format(name+' '+surname)
format6 = "{:s}".format(name)          #only string input
format7 = "{:d}".format(age)           #only decimal input
format8 = "{:b}".format(age)           #only binary input
format9 = "{:,}".format(salary)        #divite number digits

print(format1)
print(format2)
print(format3)
print(format4)
print(format5)
print(format6)
print(format7)
print(format8)
print(format9+"$")