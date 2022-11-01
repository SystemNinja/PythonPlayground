#****THIS IS MAIN VERSION, DON'T DO TESTS HERE****
#Program that calculates how many resources are needed to craft items.

choose_option=int(input("Select option:\n1-Specify how much of beer you want to make  \n2-Specify how much grain you  have\nEnter a number:"))
#input returns string value, this is another(shorter) way to make input return int value
if choose_option==1:
    material=int(input("Enter the ammount of  beer that you want to produce:"))
    #since for loop goes through values in dict, two dictionaries are needed, first dict is used for calculation, second dict is used to display names of materials
    beer = dict = {'water' : 6, 'grain' : 5, 'agent' : 2, 'sugar' : 1 } #this  dict contains the ammount of resource needed for producing beer
    mat_name= dict = {1:'Water', 2:'Grain', 3:'Agent', 4:'Sugar'} #this contains the names of resources used for producing beer
    #this little bugger plays an important role in displaying name of each resource value , instead of just number
    #what this does is, default value is first key in mat_name (water), whenever for loop iterates, this number will increase by one, therefore different name for resource will be displayed as the loop goes
    #and number of each material required for production will be attached to material name
    mat_iterator=1 
    for ammount in beer:
        total=beer[ammount]*material #multiply the number of material possessed with every value of first dict
        print("The ammount of",mat_name[mat_iterator],"you need is:",total)
        mat_iterator+=1
elif choose_option==2:
    print("Calculating the needed resources  based on ammount of grain.")
    material=int(input("Enter the ammount of  grain that you have:"))
    beer = dict = {'water' : 6, 'grain' : 5, 'agent' : 2, 'sugar' : 1 }
    total=material / beer['grain']
    print('Based on number of grain(',material,') you can produce',total,'beers')
    #print("If a number is not even, do you want to:\nLook for next higher number -  yh\n Look for next lower number - yl \n Exit - x")
else:
    print("Wrong option!")
#input("Press enter to close.\n")