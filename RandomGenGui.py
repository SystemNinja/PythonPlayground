"""
This is just plain random number generator which will generate random numbers in range from a to b.
This program will be done in the spirit of OOP on purpose!

Potential tkinter documentaiton:
http://effbot.org/tkinterbook/

How to update text of a label:
    https://stackoverflow.com/questions/17125842/changing-the-text-on-a-label
    self.<labelid>.config(text=)

Tkinter docs:
https://tkdocs.com/tutorial/firstexample.html
"""

from tkinter import *
import random

class Window(object):
    def __init__(self, window):
        self.window=window
        self.window.wm_title("Random Number Generator")
        self.window.wm_minsize(150,50)

        l1=Label(window, text="From:")
        l1.grid(row=0, column=0)
        l2=Label(window, text="To:")
        l2.grid(row=1, column=0)
        l3=Label(window, text="Result:")
        l3.grid(row=0, column=2)
        self.l4=Label(window, text="0",)
        self.l4.grid(row=1, column=2)

        self.first_value=StringVar()
        self.e1=Entry(window, width=3, textvariable=self.first_value)
        self.e1.grid(row=0, column=1)

        self.second_value=StringVar()
        self.e2=Entry(window, width=3, textvariable=self.second_value)
        self.e2.grid(row=1, column=1)

        b1=Button(window, text="Get randomness", width=12, command=self.GetNumber)
        b1.grid(row=0, column=3, rowspan=2)


    def GetNumber(self):
        a=self.first_value.get()
        b=self.second_value.get()
        try:
            rnd=random.randint(int(a),int(b))
            self.l4.config(text=rnd)
        except ValueError:
            self.l4.config(text="Action unrecongized.")

window = Tk()
Window(window)
window.mainloop()