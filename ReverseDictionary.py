"""
This is a demo program which shows tiny trick how to reverse dictionary key&values
""" 

SomeDict = {
    "a"	: "01100001",
    "b"	: "01100010",
    "c"	: "01100011",
    "d"	: "01100100",
    "e"	: "01100101",
    "f"	: "01100110"
}

#This basically goes though SomeDict and prints keys and values in reverse order -> b,a 
#Then quotes are added, colons and commas so that it can be copy/pasted into new dictionary.
#Improvise - Adapt - Overcome
for a,b in SomeDict.items():
   print("\""+b+"\"",":","\""+a+"\""+",")