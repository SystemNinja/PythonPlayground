"""
This is continuation/expansion from CliArguments.py from the same page with a little bit more advanced
tricks being shown.

Also this program will be expanded in a way that it allows it to perform other powers, not just squares
like in the first variant.

Source: https://docs.python.org/3/howto/argparse.html#getting-a-little-more-advanced

Sourde Adv: https://docs.python.org/3/library/argparse.html -- This one is real advanced version
"""

import argparse

#Instantiate parser called ArgumentParser I guess?
#To tell users what is the main purpose of the program use: description=""
parser = argparse.ArgumentParser(description="Calculate X to the power of Y.")
group = parser.add_mutually_exclusive_group()
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")

#parser.add_argument("-v", "--verbosity", action="count", default=0)
#Program is being modified due to 'group' method
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")

#Parse all arguments
args=parser.parse_args()
answer = args.x**args.y

# This example uses verbosity to change what text will be displayed
# if args.verbosity >= 2:
#     print("{} to the power {} equals {}".format(args.x, args.y, answer))
# elif args.verbosity >= 1:
#     print("{}^{} == {}".format(args.x, args.y, answer))
# else:
#     print(answer)

#Following example uses verbosity level to display more text instead
# if args.verbosity >= 2:
#     print("Running '{}'".format(__file__))
# if args.verbosity >= 1:
#     print("{}^{} == ".format(args.x, args.y), end="")
# print(answer)

# In this phase another method of argparse.ArgumentParse instance is introtuced and it is called:
# add_mutually_exclusive_group() -- It allows us to specify options that conflict with each other.
if args.quiet:
    print(answer)
elif args.verbose:
    print("{} to the power {} equals {}".format(args.x, args.y, answer))
else:
    print("{}^{} == {}".format(args.x, args.y, answer))