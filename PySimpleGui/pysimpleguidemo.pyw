'''
https://pysimplegui.readthedocs.io/en/latest/
https://pysimplegui.readthedocs.io/en/latest/cookbook/
https://github.com/PySimpleGUI/PySimpleGUI


'''
import PySimpleGUI as sg

sg.theme('DarkAmber')  # No gray windows please!

# STEP 1 define the layout
layout = [ 
            [sg.Text('This is a very basic PySimpleGUI layout')],
            [sg.Input()],
            [sg.Text('output to be changed...')],
            [sg.Button('Button'), sg.Button('Exit')]
         ]

#STEP 2 - create the window
window = sg.Window('My new window', layout, grab_anywhere=True)

# STEP3 - the event loop
while True:
    event, values = window.read()   # Read the event that happened and the values dictionary
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':     # If user closed window with X or if user clicked "Exit" button then exit
        break
    if event == 'Button':
      sg.popup('Button test')
window.close()
