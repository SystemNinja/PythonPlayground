#Command line program that performs various conversions
#This version incorporates pausing program before menu is displayed, as well as placing the output under the box made of '*'-s

import requests
from bs4 import BeautifulSoup
import os 

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

def PrettyMsg(c):
    emptySpace = " "*(len(c)+2)
    for char in range(0,5):
        if char == 2:
            print("* "+c+" *")
        elif char == 1 or char == 3:
            print("*"+emptySpace+"*")
        else:
            print("*"*(len(c)+4))

def TakeBreak():
    #Pauses program after the input so that the menu is displayed after enter is pressed
    os.system("PAUSE")

def ExitProgram():
    print("\nExiting Program.")

#CURRENCY
def GetEuroCourse():
    #Function obtains euro course from the specified site. NOTE: "Middle" course is used, referenced from National Bank of Serbia
    page = "https://www.kursna-lista.com/kursne-liste-banaka-i-menjacnica"
    GetPage = requests.get(page)
    GetPageContent = GetPage.content
    ParseContent = BeautifulSoup(GetPageContent,"html.parser")
    CourseDiv = ParseContent.find("div",{"id":"contentInner"})
    EuroCourse = ParseContent.find_all("td")[2].text
    return float(EuroCourse)

def convertEuroDin():
    euro=input("\nEnter ammount of euros:")
    try:
        convert = float(euro) * GetEuroCourse()
        result = "Euro to din conversion: "+str(convert)
        PrettyMsg(result)
        TakeBreak()
        CurrencyConverter()
    except ValueError:
        errorMsg(2)
         
def convertDinEuro():
    din = input("\nEnter ammount of dinars:")
    try:
        convert = float(din) / GetEuroCourse()
        result = "Euro to din conversion: "+str(convert)
        PrettyMsg(result)
        TakeBreak()
        CurrencyConverter()
    except ValueError:
        errorMsg(2)

#TEMPERATURE
def convertC():
    f = input("\nEnter fahrenheits:")
    try:
        celsius = (float(f)-32)*5/9
        print(f,"Fahrenheits in Celsius is:",round(celsius,2))
        TemperatureConverter()
    except ValueError:
        errorMsg(3)

def convertF():
    c = input("\nEnter celsiuses:")
    try:
        fahrenheit = float(c) * 9/5 + 32
        print(c,"Celsiuses in Fahrenheits is:",round(fahrenheit,2))
        TemperatureConverter()
    except ValueError:
        errorMsg(3)

#MASS        
def convertKg():
    lb = input("\nEnter pounds:")
    try:
        kg = float(lb) * 0.45359237
        print(lb,"Pound is equal to",round(kg,2),"Kilograms.")
        MassConverter()
    except ValueError:
        errorMsg(4)

def convertLb():
    kg = input("\nEnter kilograms:")
    try:
        lb = float(kg) / 0.45359237
        print(kg,"Kilogram is equal to",round(lb,2),"Pound.")
        MassConverter()
    except ValueError:
        errorMsg(4)

#LENGTH
def convertM():
    #Convert ft to m
    ft = input("\nEnter feets:")
    try:
        meter=float(ft) * 0.3048
        print(ft,"Feet is equal to",round(meter,2),"Meter.") 
        LengthConverter()
    except ValueError:
        errorMsg(5)

def convertFt():
    m = input("\nEnter meters:")
    try:
        feet=float(m) / 0.3048
        print(m,"Meter is equal to",round(feet,2),"Feet.")
        LengthConverter()
    except ValueError:
        errorMsg(5)

def convertCm():
    inch = input("\nEnter inches:")
    try:
        cm = float(inch) * 2.54
        print(inch,"Inch is equal to",round(cm,2),"Centimeter.")
        LengthConverter()
    except ValueError:
        errorMsg(5)

def convertInch():
    cm = input("\nEnter centimeters:")
    try:
        inch=float(cm) / 2.54
        print(cm,"Centimeter is equal to",round(inch,2),"Inch.")
        LengthConverter()
    except ValueError:
        errorMsg(5)

def convertMi():
    km = input("\nEnter kilometers:")
    try:
        miles = float(km) / 1.609344
        print(km,"Kilometer in miles is:",int(miles))
        LengthConverter()
    except ValueError:
        errorMsg(5)

def convertKm():
    mi = input("\nEnter miles:")
    try:
        kms = float(mi) * 1.609344
        print(mi,"Mile in kilometers is:",int(kms))
        LengthConverter()
    except ValueError:
        errorMsg(5)

#Handling inputs as menu options for each section, following functions are menu itself
def CurrencyConverter():
    option=str.capitalize(input("\n1 - Convert Euros to Din\n2 - Convert Din to Euro\nM:Main Menu\nChoose option:"))
    options = {
        '1' : convertEuroDin,
        '2' : convertDinEuro,
        'M' : MainMenu
    }
    #if incorrect option is selected, default option will be executed which is set as lambda
    getOpt = options.get(option, lambda: errorMsg(2))
    return getOpt()

def TemperatureConverter():
    option = str.capitalize(input("\n1 - Convert Fahrenheits to Celsius\n2 - Convert Celsius to Fahrenheit\nM:Main Menu\nChoose option:"))
    options = {
        '1' : convertC,
        '2' : convertF,
        'M' : MainMenu
    }
    getOpt = options.get(option, lambda: errorMsg(3))
    return getOpt()

def MassConverter():
    option = str.capitalize(input("\n1 - Convert kg to lb\n2 - Convert lb to kg\nM:Main Menu\nChoose option:"))
    options = {
        '1' : convertLb,
        '2' : convertKg,
        'M' : MainMenu
    }
    getOpt = options.get(option, lambda: errorMsg(4))
    return getOpt()

def LengthConverter():
    option = str.capitalize(input("\n1 - Convert m to ft\n2 - Convert ft to m\n3 - Convert cm to inch\n4 - Convert inch to cm\n5 - Convert km to miles\n6 - Convert miles to km\nM:Main Menu\nChoose option:"))
    options = {
        '1' : convertFt,
        '2' : convertM,
        '3' : convertInch,
        '4' : convertCm,
        '5' : convertMi,
        '6' : convertKm,
        'M' : MainMenu
    }
    getOpt = options.get(option, lambda: errorMsg(5))
    return getOpt()

def MainMenu():
    option = str.capitalize(input("\nAvailable programs:\n1:Currency Converter\n2:Temperature Converter\n3:Mass Converter\n4:Length Converter\nX:Exit Program\nChoose option:"))
    options = {
        '1' : CurrencyConverter,
        '2' : TemperatureConverter,
        '3' : MassConverter,
        '4' : LengthConverter,
        'X' : ExitProgram
    }
    getOpt = options.get(option, lambda: errorMsg(1))
    return getOpt()
        
#Main Program
active = True
while(active):
    #Main Menu which displays all available converions by sections
    MainMenu()
    active = False
    