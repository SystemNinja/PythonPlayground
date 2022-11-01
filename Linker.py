r"""
This program takes link for a web page, and puts it into html file which, after being opened,
by single click, a web page will be opened.

When bored, try to add feature which will sort "name" of links into alphabetic order.
"""
def Linker():
    GetLink = input("Enter link:")
    LinkName = input("Display link as(name)?")
    ParseLink = '<p><a href="'+GetLink+'">'+LinkName+'</a></p>'

    with open("Linker.html","a") as file:
        file.write("\n"+ParseLink)
Linker()
active = True
while(active):    
    question = str.capitalize(input("Add another link(Y/N)?"))
    if question == "Y":
        Linker()
    else:
        active = False