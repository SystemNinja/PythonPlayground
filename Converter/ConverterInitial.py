#Just reminder for myself
#Approximation of how program looked like before it was polished.

#Error message which will be displayed if input is bad
errorMsg = "Unrecognized action! Try again."

def CurrencyConverter(option):
    #This is non-nested version, what is difference if convertEuroDin() and convertDinEuro() were nested inside of this function
    if option == '1':
        euro=input("Enter ammount of euros:")
        convertEuroDin(euro)
    elif option == '2':
        dinar = input("Enter ammount of dinars:")
        convertDinEuro(dinar)
    else:
        print(errorMsg)

def convertEuroDin(euros):
    try:
        course = 119.643 #Current euro course
        convert = float(euros) * course
        print("Euro to din conversion:",round(convert,3))
    except ValueError:
        print(errorMsg)

def convertDinEuro(din):
    #If user enters a string instead of number, catch an ValueError exception
    try:
        course = 119.643
        convert = float(din) / course
        print("Dinar to euro conversion:",round(convert,3))
    except ValueError:
        print(errorMsg)

#Convert to celsius
def TemperatureConverter(option):
    if option == '1':
        f = input("Enter fahrenheits:")
        convertC(f)
    elif option == '2':
        c = input("Enter celsiuses:")
        convertF(c)
    else:
        print(errorMsg)
    
def convertC(f):
    try:
        celsius = (float(f)-32)*5/9
        print(f,"Fahrenheits in Celsius is:",round(celsius,2))
    except ValueError:
        print(errorMsg)

def convertF(c):
    try:
        fahrenheit = float(c) * 9/5 + 32
        print(c,"Celsiuses in Fahrenheits is:",round(fahrenheit,2))
    except ValueError:
        print(errorMsg)

#convert pounds into kilograms    
def convertKg(lb):
    try:
        kg = float(lb) * 0.45359237
        print(lb,"Pound is equal to",round(kg,2),"Kilograms.")
    except ValueError:
        print(errorMsg)

#convert kilograms into pounds
def convertLb(kg):
    try:
        lb = float(kg) / 0.45359237
        print(kg,"Kilogram is equal to",round(lb,2),"Pound.")
    except ValueError:
        print(errorMsg)

#convert ft to meters
def convertM(ft):
    try:
        meter=float(ft) * 0.3048
        print(ft,"Feet is equal to",round(meter,2),"Meter.") 
    except ValueError:
        print(errorMsg)

#convert meters to feet
def convertFt(m):
    try:
        feet=float(m) / 0.3048
        print(m,"Meter is equal to",round(feet,2),"Feet.")
    except ValueError:
        print(errorMsg)

#convert inches into cm
def convertCm(inch):
    try:
        cm = float(inch) * 2.54
        print(inch,"Inch is equal to",round(cm,2),"Centimeter.")
    except ValueError:
        print(errorMsg)
#convert cm to inch
def convertInch(cm):
    try:
        inch=float(cm) / 2.54
        print(cm,"Centimeter is equal to",round(inch,2),"Inch.")
    except ValueError:
        print(errorMsg)

#convert km to mi
def convertMi(km):
    try:
        miles = float(km) / 1.609344
        print(km,"Kilometer in miles is:",int(miles))
    except ValueError:
        print(errorMsg)

#convert mi to km 
def convertKm(mi):
    try:
        kms = float(mi) * 1.609344
        print(mi,"Mile in kilometers is:",int(kms))
    except ValueError:
        print(errorMsg)


#Main Menu which displays all available converions
"""
try:
    MainMenu = int(input("Available programs:\n1:Currency Converter\n2:Temperature converter\n3:Unit converter\nChoose option(enter a number):"))
except ValueError:
    print(errorMsg)
"""

OptionCu=input("1 - Convert Euros to Din\n2 - Convert Din to Euro\nChoose option:")
CurrencyConverter(OptionCu)
OptionTemp = input("1 - Convert Fahrenheits to Celsius\n2 - Convert Celsius to Fahrenheit\nChoose option:")
TemperatureConverter(OptionTemp)
OptionMass = input("1 - Convert kg to lb\n2 - Convert lb to kg\nChoose option:")

OptionLen = input("1 - Convert m to ft\n2 - Convert ft to m\n3 - Convert cm to inch\n4 - Convert inch to cm\n5 - Convert km to miles\n6 - Convert miles to km\nChoose option:")

feet = input("Enter feets:")
convertM(feet)
meter = input("Enter meters:")
convertFt(meter)
kg = input("Enter kilograms:")
convertLb(kg)
lb = input("Enter pounds:")
convertKg(lb)
cm = input("Enter cm's:")
convertInch(cm)
inch = input("Enter inches:")
convertCm(inch)
km = input("Enter kilometers:")
convertMi(km)
mile = input("Enter miles:")
convertKm(mile)

#Make this mandatory: keep program active under loop
"""
active = true
while(active):
    #acting commands
    #at exit:
    active = false
    #add option which will return user to main menu
    #add option which will allow user to end program without converting
    #BONUS, add option which will return user 1 step backwards
#exit
"""