import string

# Attach send input command to a list of characters, later to be converted into different string
# https://stackoverflow.com/questions/3190122/python-how-to-print-range-a-z
abc = string.ascii_uppercase
print(abc)

cmd = "SendInput "

#This will add SendINput in front of every character
for i in abc:
    print(cmd+i)

#This will print chars a-z in 1 line each
for j in abc:
    print("#"+j)