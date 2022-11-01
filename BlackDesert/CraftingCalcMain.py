#****THIS IS MAIN VERSION, DON'T DO TESTS HERE****
#Program that calculates how many resources are needed to craft items.

print("Calculating the needed resources based on ammount of grain.")
#input returns string value, this is another(shorter) way to make input return int value
material=int(input("Enter the ammount of grain that you have:"))
#since for loop goes through values in dict, two dictionaries are needed first dict is used for calculation, second dict is used to display names of materials
#Use following code if the one with names as keys won't work or is being buggy, nummbers represent following values: 1-Water 2-Grain 3-Agent 4-Sugar 
beer_num = dict = {1 : 6, 2 : 5, 3 : 2, 4 : 1 }
#beer_num = dict = {'water' : 6, 'grain' : 5, 'agent' : 2, 'sugar' : 1 } #this  dict contains the ammount of resource needed for producing beer
beer_name = dict = {1:'Water', 2:'Grain', 3:'Agent', 4:'Sugar'} #this contains the names of resources used for producing beer
#this little bugger plays an important role in displaying name of each resource value , instead of just number
#what this does is, default value is first key in mat_name (water), whenever for loop iterates, this number will increase by one, therefore different name for resource will be displayed as the loop goes
#and number of each material required for production will be attached to material name
mat_iterator = 1
#result(total_beer) is converted to int so that it returns whole number, not a decimal one 
total_beer=int(material / beer_num[2])
print("Based on number of grain:",material,"you can produce",total_beer,"beer.")
print("The recipe is as following: Grain x5, Mineral Water x6, Leavening Agent x2, Sugar x1")
print("For that ammount of beer you need following materials:")
for ammount in beer_num:
    total_mat=beer_num[ammount] * total_beer
    print(beer_name[mat_iterator],':',total_mat)
    mat_iterator+=1

input("Press enter to close.\n")
