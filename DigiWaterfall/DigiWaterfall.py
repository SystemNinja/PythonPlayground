"""
Adding colors to terminal
There are various ways, for Linux here ANSI is used. Color table: 8 bit, meaning there can be 256 colors, numbers range in 0-255.
Format for adding colors: <escape sequence>[<foreground/background code>;<color>m
Where "38;5;#m" represents foreground colors and "48;5;#m" represents background colors.
Also fg and bg do not have to be explicit, one can be omitted.
Example:
print("\033[38;5;196m \033[48;5;250m I am using 256 color table.") # Print text using bright red fg and light gray bg color.

To add aditional option such as slow blinking or bolding, just add number in front of number for color followed by ;.
Multiple options can be added this way as long as they are separated by semi-colon.
Format: ESC[<option1>;<option2>;<fg/bg>;<color>m <text>
Example:
print("\033[5;38;5;32m I am blinking slowly now.")
Options that can affect output, full list on the link below
0 	Reset / Normal - all attributes off
1 	Bold or increased intensity 	
2 	Faint (decreased intensity) 	
3 	Italic 	Not widely supported. Sometimes treated as inverse.
4 	Underline 	
5 	Slow Blink 

Contains various options like bolding, blinking, etc.
https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_parameters

List of colors: https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit
Common Colors and their values:
Black 0
Red 1
Green 2
Yellow 3
Blue 4
Magenta 5
Cyan 6
White 7
Bright Black 8
Bright Red 9
Bright Green 10
Bright Yellow 11
Bright Blue 12
Bright Magenta 13
Bright Cyan 14
Bright White 15

Random string generation
https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python

Regarding the k value which represents how many characters will be displayed:
    It depends on window size of terminal where it is opened. 
    Solution for Linux:
    Using popen from os module, process stty size can be opened and read, that process holds row and column size of a bash terminal.
    Source: https://stackoverflow.com/questions/566746/how-to-get-linux-console-window-width-in-python 
"""

import argparse
import os
import platform
import random
import string
import time


def char_waterfall(window_width): 
    # Define stream of characters which will be used.
    stream = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h j k l m n o p r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 ! @ # $ % ^ & * ( ) _ - + = * / < > ? ~"
    # Turn stream into list, separator is the space by default.
    split_stream=(stream.split())
    # Pick random character from list and make k number of random instances.
    # window_width must be converted to a number in order to be used otherwise error will be thrown if string is passed because it is NUMBER OF OCCURENCES...
    # Strip the hell out of string with .replace().
    return str(random.choices(split_stream,k=int(window_width))).replace("[","").replace("]","").replace(",","").replace(" ","").replace("'","")

def char_waterfall_binary(window_width):
    stream = [0,1]
    return str(random.choices(stream,k=int(window_width))).replace("[","").replace("]","").replace(",","").replace(" ","").replace("'","")

def color_pick(randfg=False, randbg=False, fgcolor=10, bgcolor=0):
    pickrnd_color = random.randint(0,255)
    if randfg & randbg:
        # Giving this option separate random color generators in order to avoid having always same fg and bg colors.
        pickrndfg_color = random.randint(0,255)
        pickrndbg_color = random.randint(0,255)
        return "\033[38;5;"+str(pickrndfg_color)+"m\033[48;5;"+str(pickrndbg_color)+"m"
    elif randfg:
        return "\033[38;5;"+str(pickrnd_color)+"m\033[48;5;"+str(bgcolor)+"m"
    elif randbg:
        return "\033[38;5;"+str(fgcolor)+"m\033[48;5;"+str(pickrnd_color)+"m"
    else:
        return "\033[38;5;"+str(fgcolor)+"m\033[48;5;"+str(bgcolor)+"m"

# Allow argument parsing from CLI
parser = argparse.ArgumentParser(
    # Use of formatter_class allows custom formatting of help text.
    formatter_class=argparse.RawTextHelpFormatter, 
    description="""
    Program that displays stream of random characters across the terminal window.
    Colors can be modified or set to be random and they use 8bit table.
    There are two modes, alphanumeric(default) and binary.""",
    epilog="""
    Full list of colors can be found at: https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit
    Common colors and their values:
    Black 0
    Red 1
    Green 2
    Yellow 3
    Blue 4
    Magenta 5
    Cyan 6
    White 7
    Bright Black 8
    Bright Red 9
    Bright Green 10
    Bright Yellow 11
    Bright Blue 12
    Bright Magenta 13
    Bright Cyan 14
    Bright White 15
    """)
parser.add_argument("-B", "--binary", action="store_true", help="Display characters in binary format instead of alphanumeric.")
parser.add_argument("-r", "--randomfg", action="store_true", help="When this option is used, foreground colors will be random.")
parser.add_argument("-R", "--randombg", action="store_true", help="When this option is used, background colors will be random.")
parser.add_argument("-f", "--foreground", type=int, default=10, help="Modify foreground color. Allowed values: 0-255, Default=10.")
parser.add_argument("-b", "--background", type=int, default=15, help="Modify background color. Allowed values: 0-255, Default=15.")
# Parse added arguments
args = parser.parse_args()

# Main program
while True:
    if platform.system() == 'Windows':
        terminal_width_win = os.get_terminal_size().columns #Get terminal width of windows cmd prompt.
        if args.binary:
            print(color_pick(args.randomfg, args.randombg, args.foreground, args.background)+char_waterfall_binary(terminal_width_win))
        else:
            print(color_pick(args.randomfg, args.randombg, args.foreground, args.background)+char_waterfall(terminal_width_win))
    elif platform.system() == 'Linux':
        # Get size of terminal window, two variables must be set otherwise value will be returned in form of a list
        rows, columns = os.popen('stty size', 'r').read().split()
        if args.binary:
            print(color_pick(args.randomfg, args.randombg, args.foreground, args.background)+char_waterfall_binary(columns))
        else:
            print(color_pick(args.randomfg, args.randombg, args.foreground, args.background)+char_waterfall(columns))
    else:
        print("No idea what OS are you using...")
    #This determines how fast characters will be printed on screen
    time.sleep(0.06)