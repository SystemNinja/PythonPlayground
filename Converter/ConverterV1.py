#Command line program that performs various conversions

def errorMsg(ErrorCode):
    #Assigning menu methods as values to dictionary keys
    codes = {
        1: MainMenu,
        2: CurrencyConverter,
        3: TemperatureConverter,
        4: MassConverter,
        5: LengthConverter
    }
    #Extracting the method from dictionary using key, NOTE get() is dictionary function
    func = codes.get(ErrorCode)
    #Error message which will be displayed if the input is bad
    print("\nUnrecognized action! Try again.\n")
    return func()
        
def ExitProgram():
    print("\nExiting Program.")

#CURRENCY
def convertEuroDin(euros):
    try:
        course = 119.643 #Current euro course
        convert = float(euros) * course
        print("Euro to din conversion:",round(convert,3))
        CurrencyConverter()
    except ValueError:
        errorMsg(2)  
         
def convertDinEuro(din):
    try:
        course = 119.643
        convert = float(din) / course
        print("Dinar to euro conversion:",round(convert,3))
        CurrencyConverter()
    except ValueError:
        errorMsg(2)

#TEMPERATURE
def convertC(f):
    try:
        celsius = (float(f)-32)*5/9
        print(f,"Fahrenheits in Celsius is:",round(celsius,2))
        TemperatureConverter()
    except ValueError:
        errorMsg(3)

def convertF(c):
    try:
        fahrenheit = float(c) * 9/5 + 32
        print(c,"Celsiuses in Fahrenheits is:",round(fahrenheit,2))
        TemperatureConverter()
    except ValueError:
        errorMsg(3)

#MASS        
def convertKg(lb):
    try:
        kg = float(lb) * 0.45359237
        print(lb,"Pound is equal to",round(kg,2),"Kilograms.")
        MassConverter()
    except ValueError:
        errorMsg(4)

def convertLb(kg):
    try:
        lb = float(kg) / 0.45359237
        print(kg,"Kilogram is equal to",round(lb,2),"Pound.")
        MassConverter()
    except ValueError:
        errorMsg(4)

#LENGTH
def convertM(ft):
    #Convert ft to m
    try:
        meter=float(ft) * 0.3048
        print(ft,"Feet is equal to",round(meter,2),"Meter.") 
        LengthConverter()
    except ValueError:
        errorMsg(5)

def convertFt(m):
    try:
        feet=float(m) / 0.3048
        print(m,"Meter is equal to",round(feet,2),"Feet.")
        LengthConverter()
    except ValueError:
        errorMsg(5)

def convertCm(inch):
    try:
        cm = float(inch) * 2.54
        print(inch,"Inch is equal to",round(cm,2),"Centimeter.")
        LengthConverter()
    except ValueError:
        errorMsg(5)

def convertInch(cm):
    try:
        inch=float(cm) / 2.54
        print(cm,"Centimeter is equal to",round(inch,2),"Inch.")
        LengthConverter()
    except ValueError:
        errorMsg(5)

def convertMi(km):
    try:
        miles = float(km) / 1.609344
        print(km,"Kilometer in miles is:",int(miles))
        LengthConverter()
    except ValueError:
        errorMsg(5)

def convertKm(mi):
    try:
        kms = float(mi) * 1.609344
        print(mi,"Mile in kilometers is:",int(kms))
        LengthConverter()
    except ValueError:
        errorMsg(5)

#Handling inputs as menu options for each section, following functions are menu itself
def CurrencyConverter():
    option=str.capitalize(input("\n1 - Convert Euros to Din\n2 - Convert Din to Euro\nM:Main Menu\nChoose option:"))
    if option == '1':
        euro=input("\nEnter ammount of euros:")
        convertEuroDin(euro)
    elif option == '2':
        dinar = input("\nEnter ammount of dinars:")
        convertDinEuro(dinar)
    elif option == 'M':
        MainMenu()
    else:
        errorMsg(2)

def TemperatureConverter():
    option = str.capitalize(input("\n1 - Convert Fahrenheits to Celsius\n2 - Convert Celsius to Fahrenheit\nM:Main Menu\nChoose option:"))
    if option == '1':
        f = input("\nEnter fahrenheits:")
        convertC(f)
    elif option == '2':
        c = input("\nEnter celsiuses:")
        convertF(c)
    elif option == 'M':
        MainMenu()
    else:
        errorMsg(3)

def MassConverter():
    option = str.capitalize(input("\n1 - Convert kg to lb\n2 - Convert lb to kg\nM:Main Menu\nChoose option:"))
    if option == '1':
        kg = input("\nEnter kilograms:")
        convertLb(kg)
    elif option == '2':
        lb = input("\nEnter pounds:")
        convertKg(lb)
    elif option == 'M':
        MainMenu()
    else:
        errorMsg(4)

def LengthConverter():
    option = str.capitalize(input("\n1 - Convert m to ft\n2 - Convert ft to m\n3 - Convert cm to inch\n4 - Convert inch to cm\n5 - Convert km to miles\n6 - Convert miles to km\nM:Main Menu\nChoose option:"))
    if option == '1':
        meter = input("\nEnter meters:")
        convertFt(meter)
    elif option == '2':
        feet = input("\nEnter feets:")
        convertM(feet)
    elif option == '3':
        cm = input("\nEnter centimeters:")
        convertInch(cm)
    elif option == '4':
        inch = input("\nEnter inches:")
        convertCm(inch)
    elif option == '5':
        km = input("\nEnter kilometers:")
        convertMi(km)
    elif option == '6':
        mile = input("\nEnter miles:")
        convertKm(mile)
    elif option == 'M':
        MainMenu()
    else:
        errorMsg(5)

def MainMenu():
    option = str.capitalize(input("\nAvailable programs:\n1:Currency Converter\n2:Temperature Converter\n3:Mass Converter\n4:Length Converter\nX:Exit Program\nChoose option:"))
    if option == '1':
        CurrencyConverter()
    elif option =='2':
        TemperatureConverter()
    elif option =='3':
        MassConverter()
    elif option =='4':
        LengthConverter()
    elif option == 'X':
        ExitProgram()
    else:
        errorMsg(1)
        
#Main Program
active = True
while(active):
    #Main Menu which displays all available converions by sections
    MainMenu()
    active = False