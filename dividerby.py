#this program takes certain number, divides it and returns closest number that is dividable
#without remainder
#method which calculates next highest number that returns 0 when  divided by 5
def nextHighest(n):
    division = n%5
    while division != 0:
        n-=1
        division = n%5
    return n
    
number = int(input("Enter  any number:"))
nextHighest(number)
#a way to get the result from method, just make sure it has return statement
print("real", nextHighest(number)*2)
total = number % 5
print(total)