'''
This is a slightly more complex, but more realistic version that reads input from the user and displays that input as 
text in the window. Your program is likely to be doing both of those activities so this pattern will likely be your 
starting point.
Do not worry yet what all of these statements mean. Just copy the template so you can start to experiment and discover
how PySimpleGUI programs work.

Instead of assigning key therefore changing its default value, we can use numbers as default value
without need to specify key.
'''

import PySimpleGUI as sg

sg.theme('BluePurple')

layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(15,1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('Pattern 2B', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    # Another more elegant statement to close program
    # if event in (sg.WIN_CLOSED, "Exit"):
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        # Update the "output" text element to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])

window.close()