"""
Display shapes in form of character based on number specified.
"""
def triangle(length):
    char = "*"
    empty_space = " "

    #This represents basically filled up shape
    for i in range(1,length+1):
        size=char*i
        emptyness=empty_space*(length-i)
        print(emptyness+size)
    
    #And this represents shape whose edges are made up of characters only, inside it is "empty"
    for i in range(1,length+1):#length+1 because range does not include last digit of specified range or value, w/e
        size = char*i
        emptyness = empty_space*(length-i)
        if i>2 and i<length:
            size=char+(empty_space*(i-2))+char
        print(emptyness+size)

while True:
    try:
        l = int(input("Input size:"))
        if (l > 0):
            triangle(l)
            break
        else:
            print("Number must be above 0.")
    except ValueError:
        print("You must enter a number.")