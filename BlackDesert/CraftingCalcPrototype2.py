#****PROTOTYPE 2 - For option 2 from main program****
#Program that calculates how many resources are needed to craft items.

def nextHighest(n,o):
    division = n%5
    while division != 0:
        if o=="h":
            n+=1
        else:
            n-=1
        division = n%5
    return n 

print("Calculating the needed resources  based on ammount of grain.")
material=int(input("Enter the ammount of  grain that you have:"))
beer = dict = {'water' : 6, 'grain' : 5, 'agent' : 2, 'sugar' : 1 }
total=material / beer['grain']
print('Based on number of grain(',material,')you can produce',total,'beers')
print("If a number is not even, do you want to:\nLook for next higher number - h\nLook for next lower number - l \nExit - x")
opt=str.lower(input("Choose option:"))
if opt=='h':
    nextHighest(material,opt)
elif opt=='l':
    nextHighest(material,opt)
else:
    print("Wrong option!")

#input("Press enter to close.\n") #disabled  during testing phase