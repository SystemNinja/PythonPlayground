#Command line program that performs various conversions
#In this version of program, if-else is replaced with assinging methods as values to dictionary keys

import requests
from bs4 import BeautifulSoup
import os 

def ErrorMsg(ErrorCode):
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
def GetEuroCourse():
    #Function obtains euro course from the specified site. NOTE: "Middle" course is used, referenced from National Bank of Serbia
    page = "https://www.kursna-lista.com/kursne-liste-banaka-i-menjacnica"
    GetPage = requests.get(page)
    GetPageContent = GetPage.content
    ParseContent = BeautifulSoup(GetPageContent,"html.parser")
    CourseDiv = ParseContent.find("div",{"id":"contentInner"})
    EuroCourse = ParseContent.find_all("td")[2].text
    return float(EuroCourse)

def ConvertEuroDin():
    euro=input("\nEnter ammount of euros:")
    try:
        convert = float(euro) * GetEuroCourse()
        print("Euro to din conversion:",convert,"\n")
        CurrencyConverter()
    except ValueError:
        ErrorMsg(2)
         
def ConvertDinEuro():
    din = input("\nEnter ammount of dinars:")
    try:
        convert = float(din) / GetEuroCourse()
        print("Dinar to euro conversion:",round(convert,3))
        CurrencyConverter()
    except ValueError:
        ErrorMsg(2)

#TEMPERATURE
def ConvertC():
    f = input("\nEnter fahrenheits:")
    try:
        celsius = (float(f)-32)*5/9
        print(f,"Fahrenheits in Celsius is:",round(celsius,2))
        TemperatureConverter()
    except ValueError:
        ErrorMsg(3)

def ConvertF():
    c = input("\nEnter celsiuses:")
    try:
        fahrenheit = float(c) * 9/5 + 32
        print(c,"Celsiuses in Fahrenheits is:",round(fahrenheit,2))
        TemperatureConverter()
    except ValueError:
        ErrorMsg(3)

#MASS        
def ConvertKg():
    lb = input("\nEnter pounds:")
    try:
        kg = float(lb) * 0.45359237
        print(lb,"Pound is equal to",round(kg,2),"Kilograms.")
        MassConverter()
    except ValueError:
        ErrorMsg(4)

def ConvertLb():
    kg = input("\nEnter kilograms:")
    try:
        lb = float(kg) / 0.45359237
        print(kg,"Kilogram is equal to",round(lb,2),"Pound.")
        MassConverter()
    except ValueError:
        ErrorMsg(4)

#LENGTH
def ConvertM():
    #Convert ft to m
    ft = input("\nEnter feets:")
    try:
        meter=float(ft) * 0.3048
        print(ft,"Feet is equal to",round(meter,2),"Meter.") 
        LengthConverter()
    except ValueError:
        ErrorMsg(5)

def ConvertFt():
    m = input("\nEnter meters:")
    try:
        feet=float(m) / 0.3048
        print(m,"Meter is equal to",round(feet,2),"Feet.")
        LengthConverter()
    except ValueError:
        ErrorMsg(5)

def ConvertCm():
    inch = input("\nEnter inches:")
    try:
        cm = float(inch) * 2.54
        print(inch,"Inch is equal to",round(cm,2),"Centimeter.")
        LengthConverter()
    except ValueError:
        ErrorMsg(5)

def ConvertInch():
    cm = input("\nEnter centimeters:")
    try:
        inch=float(cm) / 2.54
        print(cm,"Centimeter is equal to",round(inch,2),"Inch.")
        LengthConverter()
    except ValueError:
        ErrorMsg(5)

def ConvertMi():
    km = input("\nEnter kilometers:")
    try:
        miles = float(km) / 1.609344
        print(km,"Kilometer in miles is:",int(miles))
        LengthConverter()
    except ValueError:
        ErrorMsg(5)

def ConvertKm():
    mi = input("\nEnter miles:")
    try:
        kms = float(mi) * 1.609344
        print(mi,"Mile in kilometers is:",int(kms))
        LengthConverter()
    except ValueError:
        ErrorMsg(5)

#Handling inputs as menu options for each section, following functions are menu itself
def CurrencyConverter():
    option=str.capitalize(input("\n1 - Convert Euros to Din\n2 - Convert Din to Euro\nM:Main Menu\nChoose option:"))
    options = {
        '1' : ConvertEuroDin,
        '2' : ConvertDinEuro,
        'M' : MainMenu
    }
    #if incorrect option is selected, default option will be executed which is set as lambda
    getOpt = options.get(option, lambda: ErrorMsg(2))
    return getOpt()

def TemperatureConverter():
    option = str.capitalize(input("\n1 - Convert Fahrenheits to Celsius\n2 - Convert Celsius to Fahrenheit\nM:Main Menu\nChoose option:"))
    options = {
        '1' : ConvertC,
        '2' : ConvertF,
        'M' : MainMenu
    }
    getOpt = options.get(option, lambda: ErrorMsg(3))
    return getOpt()

def MassConverter():
    option = str.capitalize(input("\n1 - Convert kg to lb\n2 - Convert lb to kg\nM:Main Menu\nChoose option:"))
    options = {
        '1' : ConvertLb,
        '2' : ConvertKg,
        'M' : MainMenu
    }
    getOpt = options.get(option, lambda: ErrorMsg(4))
    return getOpt()

def LengthConverter():
    option = str.capitalize(input("\n1 - Convert m to ft\n2 - Convert ft to m\n3 - Convert cm to inch\n4 - Convert inch to cm\n5 - Convert km to miles\n6 - Convert miles to km\nM:Main Menu\nChoose option:"))
    options = {
        '1' : ConvertFt,
        '2' : ConvertM,
        '3' : ConvertInch,
        '4' : ConvertCm,
        '5' : ConvertMi,
        '6' : ConvertKm,
        'M' : MainMenu
    }
    getOpt = options.get(option, lambda: ErrorMsg(5))
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
    getOpt = options.get(option, lambda: ErrorMsg(1))
    return getOpt()
        
#Main Program
while True:
    #Main Menu which displays all available converions by sections
    MainMenu()
    break
    