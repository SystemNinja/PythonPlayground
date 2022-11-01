#This program converts text into NATO alphabet

#This will be used to set delay for line execution
# https://stackoverflow.com/questions/510348/how-can-i-make-a-time-delay-in-python 
# https://www.pythoncentral.io/pythons-time-sleep-pause-wait-sleep-stop-your-code/ 

#Set Window Title
#https://stackoverflow.com/questions/7387276/set-windows-command-line-terminal-title-in-python 

from time import sleep
import os
import platform

alphabet = {
    "a" : "Alpha",
    "b" : "Bravo",
    "c" : "Charlie",
    "d" : "Delta",
    "e" : "Echo",
    "f" : "Foxtrot",
    "g" : "Golf",
    "h" : "Hotel",
    "i" : "India",
    "j" : "Juliet",
    "k" : "Kilo",
    "l" : "Lima",
    "m" : "Mike",
    "n" : "November",
    "o" : "Oscar",
    "p" : "Papa",
    "q" : "Quebec",
    "r" : "Romeo",
    "s" : "Sierra",
    "t" : "Tango",
    "u" : "Uniform",
    "v" : "Victor",
    "w" : "Whiskey",
    "x" : "X-ray",
    "y" : "Yankee",
    "z" : "Zulu",
    " " : " "
}

def program():
    text = str.lower(input("Enter the text or name to be converted:"))
    ProcessTxt=list(text)        
    if platform.system() == "Windows":
        os.system("cls") #clear the terminal and then print results
    else:
        os.system("clear") #this one is for linux
    
    for char in ProcessTxt:
        print(alphabet.get(char))
    print("\n")

active=True
while active: 
    program()
    choice = str.lower(input("Continue(Y/N)?"))
    if choice=="y":
        program()
    elif choice=="n":
        print("\nProgram will now exit.\n")
        #sleep(3) #Delay execution of line below for # of seconds)
        active=False
    else:
        print("Invalid option, restart the program.\n\n")
        break