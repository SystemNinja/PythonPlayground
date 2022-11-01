active = True

def errorMsg():
    #Error message which will be displayed if the input is bad
    print("Unrecognized action! Try again.")

#CURRENCY
def convertEuroDin(euros):
    try:
        course = 119.643 #Current euro course
        convert = float(euros) * course
        print("Euro to din conversion:",round(convert,3))
    except ValueError:
        errorMsg()
         

def convertDinEuro(din):
    try:
        course = 119.643
        convert = float(din) / course
        print("Dinar to euro conversion:",round(convert,3))
    except ValueError:
        errorMsg()

#TEMPERATURE
def convertC(f):
    try:
        celsius = (float(f)-32)*5/9
        print(f,"Fahrenheits in Celsius is:",round(celsius,2))
    except ValueError:
        errorMsg()

def convertF(c):
    try:
        fahrenheit = float(c) * 9/5 + 32
        print(c,"Celsiuses in Fahrenheits is:",round(fahrenheit,2))
    except ValueError:
        errorMsg()

#MASS        
def convertKg(lb):
    try:
        kg = float(lb) * 0.45359237
        print(lb,"Pound is equal to",round(kg,2),"Kilograms.")
    except ValueError:
        print(errorMsg)

def convertLb(kg):
    try:
        lb = float(kg) / 0.45359237
        print(kg,"Kilogram is equal to",round(lb,2),"Pound.")
    except ValueError:
        print(errorMsg)

#LENGTH
def convertM(ft):
    #Convert ft to m
    try:
        meter=float(ft) * 0.3048
        print(ft,"Feet is equal to",round(meter,2),"Meter.") 
    except ValueError:
        print(errorMsg)

def convertFt(m):
    try:
        feet=float(m) / 0.3048
        print(m,"Meter is equal to",round(feet,2),"Feet.")
    except ValueError:
        print(errorMsg)

def convertCm(inch):
    try:
        cm = float(inch) * 2.54
        print(inch,"Inch is equal to",round(cm,2),"Centimeter.")
    except ValueError:
        print(errorMsg)

def convertInch(cm):
    try:
        inch=float(cm) / 2.54
        print(cm,"Centimeter is equal to",round(inch,2),"Inch.")
    except ValueError:
        print(errorMsg)

def convertMi(km):
    try:
        miles = float(km) / 1.609344
        print(km,"Kilometer in miles is:",int(miles))
    except ValueError:
        print(errorMsg)

def convertKm(mi):
    try:
        kms = float(mi) * 1.609344
        print(mi,"Mile in kilometers is:",int(kms))
    except ValueError:
        print(errorMsg)

#Handling inputs as menu options for each section, following functions are menu itself
def CurrencyConverter(option):
    if option == '1':
        euro=input("Enter ammount of euros:")
        convertEuroDin(euro)
    elif option == '2':
        dinar = input("Enter ammount of dinars:")
        convertDinEuro(dinar)
    else:
        errorMsg()

def TemperatureConverter(option):
    if option == '1':
        f = input("Enter fahrenheits:")
        convertC(f)
    elif option == '2':
        c = input("Enter celsiuses:")
        convertF(c)
    else:
        errorMsg()

def MassConverter(option):
    if option == '1':
        kg = input("Enter kilograms:")
        convertLb(kg)
    elif option == '2':
        lb = input("Enter pounds:")
        convertKg(lb)
    else:
        errorMsg()        

def LengthConverter(option):
    if option == '1':
        meter = input("Enter meters:")
        convertFt(meter)
    elif option == '2':
        feet = input("Enter feets:")
        convertM(feet)
    elif option == '3':
        cm = input("Enter centimeters:")
        convertInch(cm)
    elif option == '4':
        inch = input("Enter inches:")
        convertCm(inch)
    elif option == '5':
        km = input("Enter kilometers:")
        convertMi(km)
    elif option == '6':
        mile = input("Enter miles:")
        convertKm(mile)
    else:
        errorMsg()

def MainMenu(option):
    if option == '1':
        OptionCu=input("1 - Convert Euros to Din\n2 - Convert Din to Euro\nChoose option:")
        CurrencyConverter(OptionCu)
    elif option =='2':
        OptionTemp = input("1 - Convert Fahrenheits to Celsius\n2 - Convert Celsius to Fahrenheit\nChoose option:")
        TemperatureConverter(OptionTemp)
    elif option =='3':
        OptionMass = input("1 - Convert kg to lb\n2 - Convert lb to kg\nChoose option:")
        MassConverter(OptionMass)
    elif option =='4':
        OptionLen = input("1 - Convert m to ft\n2 - Convert ft to m\n3 - Convert cm to inch\n4 - Convert inch to cm\n5 - Convert km to miles\n6 - Convert miles to km\nChoose option:")
        LengthConverter(OptionLen)
    elif option == 'X':
        print("\nExiting Program.")
        active = False
    else:
        errorMsg()





#Make this mandatory: keep program active under loop

while(active):
    #Main Menu which displays all available converions by sections
    Menu = str.capitalize(input("Available programs:\n1:Currency Converter\n2:Temperature Converter\n3:Mass Converter\n4:Lenbth Converter\nX:Exit\nChoose option:"))
    print("")
    MainMenu(Menu)
    active = False
    #acting commands
    #at exit:
    #active = false
    #add option which will return user to main menu
    #add option which will allow user to end program without converting
    #BONUS, add option which will return user 1 step backwards


