#This program demonstrates usage of lambda function  http://www.secnetix.de/olli/Python/lambda_functions.hawk
#Lambda in its core is a function that is not bound to a name. It does not contain return statement, instead it contains expression 
# which is always returned.
#For the time being, don't bother with it too much, just know its existence

#Example#1
#Technicaly the function takes 2 parameters
#This defines function incrementor, requests one argument, anonymously, second function -> lambda is created which increments n by value specified as second separate argument 
def incrementor(n):
    return lambda x: x+n

#Assigning fuction to a,b,c and passing first parameter
a=incrementor(1)
b=incrementor(2)
c=incrementor(3)

#Calling functions a,b,c and assigning second parameter
print(a(10),b(10),c(10))
#Directly calling function without assigning it to a variable and printing its result
print(incrementor(5)(2))

#Example#2
#Note functions in this example are a bit outdated, so they shouldn't be used unless it's a really a must.
#Nonetheless, they only serve as example for lambda function. Suggested workaround is to use generator expression.

#filter function - https://www.programiz.com/python-programming/methods/built-in/filter
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

#In python3, filter expects true or false to be returned from a list, when in filter, foo is considered an filter object
#that's why, in order to print result from filter, it needs to be returned as list.
#Long story short, in order to print result from filter,map,
print(list(filter(lambda x: x % 3 == 0, foo)))
#For each element in list foo, map function performs computation defined by lambda
print(list(map(lambda x: x*2+10,foo)))
