import random
import time 
import os
import string
import platform
from colorama import Fore, Back, Style

binary = [0,1]
junk = ['[',',',']',' ']

while True:
    RandItem = str(random.choices(binary, k=128))

    for i in range(len(junk)):
        print(RandItem.replace(junk[i],""))
    #print(Fore.GREEN+Result)
    
    time.sleep(0.07)
    break