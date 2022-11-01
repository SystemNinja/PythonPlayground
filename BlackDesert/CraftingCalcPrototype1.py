#****PROTOTYPE 1 - For option 1 from main program****
#Program that calculates how many resources are needed to craft items.
def nextHighest(n):
    division = n%5
    while division != 0:
        n+=1
        division = n%5
    return n

material=int(input("Enter the ammount of  beer that you want to produce:"))
#Use following code if the one with names as keys won't work or is being buggy
#beer_num = dict = {1 : 6, 2 : 5, 3 : 2, 4 : 1 } 
beer_num = dict = {'water' : 6, 'grain' : 5, 'agent' : 2, 'sugar' : 1 } 
beer_name = dict = {1:'Water', 2:'Grain', 3:'Agent', 4:'Sugar'} 
mat_iterator=1 
for ammount in beer_num:
    total=beer[ammount]*material
    print("The ammount of",mat_name[mat_iterator],"you need is:",total)
    mat_iterator+=1
#input("Press enter to close.\n") #disabled  during testing phase

