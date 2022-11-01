"""
This program has an infinite loop with no break statement inside. 
The only way this program will end is if the user enters
exit, causing sys.exit() to be called. When response is equal to exit, the program
ends. Since the response variable is set by the input() function, the user
must enter exit in order to stop the program.
"""

import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
