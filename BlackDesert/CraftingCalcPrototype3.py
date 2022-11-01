#****PROTOTYPE 2 - For option 2 from main program****
#Program that calculates how many resources are needed to craft items.
def nextValidNum(n):
    division = n%5
    while division != 0:
        n-=1
        division = n%5    
    return n 
#Program starts here!!!
print("Calculating the needed resources based on ammount of grain.")
material=int(input("Enter the ammount of  grain that you have:"))
beer_num = dict = {'water' : 6, 'grain' : 5, 'agent' : 2, 'sugar' : 1 } 
beer_name = dict = {1:'Water', 2:'Grain', 3:'Agent', 4:'Sugar'}
mat_iterator = 1
total_beer=material / beer_num['grain']
print("based on number of grain(",material,")you can produce',total_beer,'beer.\nfor that ammount of beer you need following materials:")
for ammount in beer_num:
    total_mat=beer_num[ammount] * total_beer
    print(beer_name[mat_iterator],':',total_beer)
    mat_iterator+=1


#print("If a number is not even, do you want to:\nLook for next higher number - h\nLook for next lower number - l \nExit - x")
#opt=str.lower(input("Choose option:"))
#if opt=='h':
#    nextHighest(material,opt)
#elif opt=='l':
#    nextHighest(material,opt)
#else:
#    print("Wrong option!")

#input("Press enter to close.\n") #disabled  during testing phase