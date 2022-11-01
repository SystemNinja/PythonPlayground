r"""
Generate password using words from english dictionary.
Requirements:
-Total number of characters must be at least 8 or 9
-Words will start with first capital letter, if password has more than one word, first letter of each will be uppercase
-Must contain one of the symbols: ! @ #
-Must contain one number


Get list from dictionary by picking key value and get value from list using index.
print(pick_list.get(1)[4])

Test output with multiple entries writen to a file:
with open("test-output.txt", "a") as file1:
    n = 0
    while (n <= 100):
        gen_number = random.randint(1, 99)
        output = rand_words[random.randint(0, len(rand_words)-1)].capitalize()+symbols[random.randint(0, len(symbols)-1)]+str(gen_number)
        file1.writelines(output+"\n")
        n+=1


GUI references:
https://www.python-course.eu/tkinter_layout_management.php
https://stackoverflow.com/questions/3842155/is-there-a-way-to-make-the-tkinter-text-widget-read-only 

"""

import random
import os
from tkinter import *

def generate_password():
    colors = ['red', 'green', 'yellow', 'white', 'blue', 'black', 'pink', 'purple', 'cyan', 'gray', 'silver', 'orange', 'brown']
    animals = ['fox', 'wolf', 'eagle', 'tiger', 'parrot', 'lion']
    rand_words = ['sky', 'grass', 'tree', 'leaf', 'rain', 'rainy', 'fire', 'fiery']
    symbols = ['!', '@', '#']
    gen_number = random.randint(1, 99)

    # place above arrays into dictionary
    pick_list = {
        1: colors,
        2: animals,
        3: rand_words
    }

    pick_list_seed = random.randint(1,3)

    output = pick_list.get(pick_list_seed)[random.randint(0, len(pick_list.get(pick_list_seed))-1)].capitalize()+symbols[random.randint(0, len(symbols)-1)]+str(gen_number)
    if (len(output) < 9):
        dice = random.randint(1, 3)
        if(dice == 1): # print colors+animals 
            output = pick_list.get(1)[random.randint(0, len(pick_list.get(1))-1)].capitalize()+pick_list.get(2)[random.randint(0, len(pick_list.get(2))-1)].capitalize()+symbols[random.randint(0, len(symbols)-1)]+str(gen_number)
        elif(dice == 2): # print colors+rand_words
            output = pick_list.get(1)[random.randint(0, len(pick_list.get(1))-1)].capitalize()+pick_list.get(3)[random.randint(0, len(pick_list.get(3))-1)].capitalize()+symbols[random.randint(0, len(symbols)-1)]+str(gen_number)
        elif(dice == 3): #print rand_words+animals
            output = pick_list.get(3)[random.randint(0, len(pick_list.get(3))-1)].capitalize()+pick_list.get(2)[random.randint(0, len(pick_list.get(2))-1)].capitalize()+symbols[random.randint(0, len(symbols)-1)]+str(gen_number)
        else:
            pass
    
    #Displaying results onto the text fields
    t1.configure(state="normal")
    #Purpose of delete is to remove previous entry and generate new output if value has been changed
    #Without delete, text fields will retain values from the first conversion
    t1.delete("1.0", END)
    t1.insert(END, output)
    t1.configure(state="disabled")

# generate_password()

window = Tk()
window.title("Password Generator Tkinter")

#Window size
w=260
h=50

ws=window.winfo_screenwidth() #get screen width
hs=window.winfo_screenheight() #get screen height

#Calculate x and y coordinates for the Tk window, this shit is used when you want to make window appear in middle of screen
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

#This shit controls position of a window height and width can be ommited 
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

t1 = Text(window, state="disabled", height=1, width=15)
t1.pack()

b1 = Button(window, text="Generate", command=generate_password)
# b1.grid(row = 0, column = 1)
b1.pack()

window.mainloop()