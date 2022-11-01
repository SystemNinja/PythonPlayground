import random
import time 
import os
import string
import platform

def ColorPicker(size=1, color=string.hexdigits):
    return ''.join(random.choice(color) for i in range(size))

def ColorPickerLinux():
    ColorList = [30,31,32,33,34,35,36,37,38,39,90,91,92,93,94,95,96,97,98,99]
    CurrentColor = random.choice(ColorList)
    if(CurrentColor != 30):
        return "\033[53;"+str(CurrentColor)+"m"
    else:
        return ""

binary = [0,1]

#Get size of terminal window, two variables must be set otherwise value will be returned in form of a list
#rows, columns = os.popen('stty size', 'r').read().split()

while True:
    RandItem = str(random.choices(binary, k=int(columns)))
    Result = RandItem.replace("[","").replace("]","").replace(",","").replace(" ","")
    
    #Change color of windows cmd prompt and display text in that color
    if platform.system() == 'Windows':
        print(Result)
        os.system('color 0'+ColorPick(color="0A"))
    else:
        #print("\033[92m\033[40m"+Result)
        print(ColorPickerLinux()+Result)
    time.sleep(0.07)
