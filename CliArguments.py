"""
This program showcases how to add arguments to CLI python script.

Note: 
-h is available by default without writing any extra code.

Source:
https://docs.python.org/3/howto/argparse.html

https://docs.python.org/3/library/argparse.html -- This one is real advanced version
"""

import argparse

#Instantiate parser?
parser = argparse.ArgumentParser()

"""
Adds mandatory  positional argument called test1 which takes some value as argument when program is called.
Positional argument is basically argument that must be used at 'n' position. test1 is first argument.
help - displays additional info when -h argument is added
"""
#parser.add_argument("test1", help="echo or write the string you use here")

#Make argument do something useful. Type must be set to int because argparse treats given options as strings.
parser.add_argument("square", help="display a square of a given number", type=int)

"""
Add optional argument
action="store_true" -- This means that when --verbose is called, set value of args.verbose to True
it basically turned --verbose into more like a flag, meaning it does not need a value to be specified
when it is called and program will complain when value is specified.
Actual cmd:parser.add_argument("-v","--verbose", help="increase output verbosity", action="store_true")
**ALSO, when optional argument --verbose is used, args.verbose==True otherwise it is False.
Google what are flags...

To add short option to optional argument add it before specifying name of argument starting with --
short option starts with single dash(-). Now instead of typing --v or --verbose, just type -v.

Third phase?? Giving back option to have multiple verbosity values and utilize them.
Atm numbers 1 and 2 were used to determine how the output will look like but it exposes a bug which allowed
any number to be used.

Fourth phase -- Restrict values --verbose can accept. Which is done with choices=[] parameter.
"""
# parser.add_argument("-v","--verbose", type=int, choices=[1,2], help="increase output verbosity")

"""
This example demonstrates different approach to playing with verbosity. 
It matches the way CPython executable handles its own verbosity argument.

action="count" - Count the number of occurences of a specific optional arguments.
Ex: -v == 1, -vv == 2 || --verbose --verbose == 2
Note: Adding value after the argument will throw an error.
default=0 sets default value to argument
"""
parser.add_argument("-v","--verbose", action="count", default=0, help="increase output verbosity by counting occurences of argument -v or --v")

#parse_args() returns data from specified options, that value is then assigned to args variable
#other way to write output of first argument called test1 would be: parser.parse_args().test1
args = parser.parse_args()

#Print the value of argument specified as first parameter of add_argument()
# print(args.test1 + " - First example.\n")
# print(args.square**2, " - Second example. \n")

#Combining optional and positional args. Order of args in this case does not matter.

#calculate square and assign it to answer
answer = args.square**2

"""
bugfix: replace == with >=. This will handle situations such as when -vvv is used.
bugfix2: after first bugfix if optional argument was not entered, program would throw an error.
The reason why error is thrown is because value of args.verbose is set to None,
which cannot be compared to int an value.
solution to bugfix2: set default value to an optional argument verbose.
"""
if args.verbose >= 2:
    print("the square of {} equals {}".format(args.square, answer))
elif args.verbose >= 1:
    print("{}^2 == {}".format(args.square, answer))
else:
    print(answer)