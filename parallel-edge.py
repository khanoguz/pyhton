def rightslash(count):
    for i in range(int(count)):
        print("/",end="")

def leftslash(count):
    for i in range(int(count)):
        print("\\",end="")

def bttmline(count):
    for i in range(int(count)):
        print()

def space(count):
    for i in range(int(count)):
        print(" ",end="")

def upsize(dia):
    firstspace = dia/2-1
    for i in range(int(dia/2)):
        space(firstspace-i)
        rightslash(1)
        space(i*2)
        leftslash(1)
        bttmline(1)

def downsize(dia):
    firstspace = dia -2
    for i in range(int(dia/2)):
        space(i)
        leftslash(1)
        space(firstspace - i*2)
        rightslash(1)
        bttmline(1)
        
def show(dia):
    upsize(dia)
    downsize(dia)

show(40)