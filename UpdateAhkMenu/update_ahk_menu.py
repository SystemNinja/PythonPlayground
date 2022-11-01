r"""
Program that is supposed to automate adding menu entries into ahk script

Reference:
https://www.adamsmith.haus/python/answers/how-to-edit-a-specific-line-in-a-text-file-in-python
https://stackoverflow.com/questions/4719438/editing-specific-line-in-text-file-in-python
https://www.adamsmith.haus/python/answers/how-to-append-a-newline-to-a-file-in-python

Script path:
C:\Users\white\OneDrive - Setton Consulting Inc\scripts\BlackMagic.ahk

Steps to accomplish task:
where to create/add menu under which menu/submenu
add it for now at the end of the submenu/last command
"""


with open(r"C:\Users\white\OneDrive - Setton Consulting Inc\scripts\BlackMagic.ahk", "r+") as f:
    file = f.readlines()
    file_size = len(file)-1
    start_pos = file[14]

    print(file[file_size])
    # if(file[file_size] == "Return"):
    #     print("True or w/e")
    # else:
    #     print("Didn't work\n\n")

print(file[0])