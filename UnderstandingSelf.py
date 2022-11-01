"""
This program serves as example of understanding self in OOP


To try and explain it meself with words.
Ex what instances are:
obj1 = SomeClass() # This is instance '1'
obj2 = SomeClass() # This is instance '2'

Sooooo when class is instantiated or instances have been made, if we say:
obj1.InsertToArr(5)
obj2.InsertToArr(3)
aaand when objx.arr is printed, values will be different, and program knows that thanks to the self.
Self points to instance of a class so, unique value of arr will be added to obj1 in this case 5 and to obj2, 3 will be added.


Ref:
https://medium.com/quick-code/understanding-self-in-python-a3704319e5f0
https://pythontips.com/2013/08/07/the-self-variable-in-python-explained/ 
"""


class SomeClass:
    def CreateArr(self): # An instance method
        self.arr = []

    def InsertToArr(self, value): #An instance method
        self.arr.append(value)

obj3 = SomeClass()
obj3.CreateArr()
obj3.InsertToArr(5)
print(obj3.arr)