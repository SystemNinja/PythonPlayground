'''
This program demonstrates how to create alias
Alias basically allows one command to be shortened or to have other custom name
This can eliminate need to type sg. before each cmd
'''
import PySimpleGUI as sg

sg.theme('DarkAmber')    # Keep things interesting for your users

# Create variable and assign command as value
txt = sg.Text

layout = [[txt('Persistent window')], # Execute sg.Text() command by using alias txt
          [sg.Input(key='-IN-')],
          [sg.Button('Read'), sg.Exit()]]

window = sg.Window('Window that stays open', layout)

while True:                             # The Event Loop
    event, values = window.read()
    print(event, values) #very useful for debugging
    # Another more elegant statement to close program
    # if event in (sg.WIN_CLOSED, "Exit"):
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()