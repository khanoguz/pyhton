"""
open a exising file
file = open("/sys/class/power_supply/BAT1/capacity")
data = file.read()
file.close()
print(data)
"""

"""
writing data to file
#file = open("try.txt","w")
#writing = "Hello im oğuz kağan and im learning python"
#file.write(writing)
file.close()
"""
"""
reading data to file

file = open("try.txt","r")

reading = file.readlines()

print(reading)

"""
"""
some syntax

'r' --> for reading
'w' --> for writing
'a' --> for writing (if there is file,it continue to write, if not it create new file)
'x' --> for writing (if there is file, it gives error)

'r+' --> writing and reading (file must be existing)
'w+' --> writing and reading (if there is file,deletes and create again)
'a+' --> writing and reading
'x+' --> writing and reading

"""