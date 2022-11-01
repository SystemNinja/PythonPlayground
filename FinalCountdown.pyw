"""
This program tells how many days I have until my contract at NCR expires.

.pyw extension is used to suppress the console

Reference:
https://stackoverflow.com/questions/7628036/how-much-days-left-from-today-to-given-date 
http://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html 
https://stackoverflow.com/questions/14910858/how-to-specify-where-a-tkinter-window-opens/14910894#14910894
https://stackoverflow.com/questions/1918005/making-python-tkinter-label-widget-update
https://stackoverflow.com/questions/35921520/python-tkinter-label?rq=1
http://robotic-controls.com/learn/python-guis/making-gui-attractive
https://stackoverflow.com/questions/1892339/how-to-make-a-tkinter-window-jump-to-the-front

Errors:
https://stackoverflow.com/questions/31186125/tkinter-displays-text-with
https://stackoverflow.com/questions/47855811/removing-curly-brackets-from-tkinter-label

Console Version:
Today=date.today()
ContractExpires=date(2018, 10, 31)

#diff is a timedelta object
diff=ContractExpires-Today

print(diff.days,"days left.")
"""

from datetime import date
from tkinter import *


def FinalCountdown():
    Today=date.today()
    ContractExpires=date(2020, 12, 31)
    diff = ContractExpires-Today
    return diff.days

window = Tk()
window.title("Final Countdown")
window.configure(background="black") #configure window to change bg color
#window.overrideredirect(1) #this one would remove all controls from window and make it unable to be selected or even hardly found in task manager, terminal is the only thing that is connected to it
#This makes window/program always stay on top of other windows, can be minimized
window.attributes("-topmost", True)

#Window size
w=260
h=50

ws=window.winfo_screenwidth() #get screen width
hs=window.winfo_screenheight() #get screen height

#Calculate x and y coordinates for the Tk window, this shit is used when you want to make window appear in middle of screen
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

#takes resolution of primary monitor then add or remove numbers to move window to secondary monitor or primary
# x = ws-6.1
# y = hs-213

#This shit controls position of a window height and width can be ommited 
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

#Method was resolved to a variable msg and converted to string then used string concatenation because:
#without this workaround aka when variable that is not of a string type is referenced, python will wrap text with { }
msg=str(FinalCountdown())+" Days Left."

l1=Label(window, text=msg, justify=CENTER, anchor=CENTER, bg="black", fg="yellow",font=("Times New Roman", 24), height=5)
l1.pack()

window.mainloop()