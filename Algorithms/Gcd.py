#Calculate GCD using Euclid's Algorithm

def gcd(a,b):
    while (b != 0):
       t = a
       a = b
       b = t % b
    
    return a

def gcd1():
    pass



print(gcd(20,8))
print(gcd(65,28))