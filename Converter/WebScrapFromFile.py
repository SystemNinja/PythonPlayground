#Attempts to download page in form of html and parse data from file
#Timer is to be added so that download is performed once a day only 
#Goal is to increase speed at which result will be returned

import requests
from bs4 import BeautifulSoup
import time

def GetEuroCourse():
    #Function obtains euro course from the specified site. NOTE: "Middle" course is used, referenced from National Bank of Serbia
    page = "https://www.kursna-lista.com/kursne-liste-banaka-i-menjacnica"
    GetPage = requests.get(page)
    GetPageContent = GetPage.content
    ParseContent = BeautifulSoup(GetPageContent,"html.parser")
    with open("D:\Python\Blablabla\TestFairu.txt",'w+', encoding="utf-16") as file:
        file.write(str(ParseContent))

    CourseDiv = ParseContent.find("div",{"id":"contentInner"})
    EuroCourse = ParseContent.find_all("td")[2].text
    return float(EuroCourse)

#GetEuroCourse()

page = "https://www.kursna-lista.com/kursne-liste-banaka-i-menjacnica"
GetPage = requests.get(page)
GetPageContent = GetPage.content


start = time.time()

#a = range(100000)
#b = [i*2 for i in a]

with open("D:\Python\Blablabla\TestFairu.txt",'r', encoding='utf-16') as WriteFile:
    #WriteFile.write(str(GetPageContent))
    content = WriteFile.readlines()

for i,line in enumerate(content):
    if i == 175:
        print(line)

end = time.time()
print(round(end - start,4))


"""
with open("D:\Python\Blablabla\TestFairu1.txt",'r') as ReadFile:
    ParseContent = BeautifulSoup(ReadFile,"html.parser")
CourseDiv = ParseContent.find("div",{"id":"contentInner"})
EuroCourse = ParseContent.find_all("td")[2].text

print("Random stuff")
print(float(EuroCourse)*10)
"""
"""
with open("D:\Python\Blablabla\TestFairu1.txt",'r', encoding='utf-16') as ReadFile1:
    ReadFile1.seek(0)
    content = ReadFile1.readlines()

for i,line in enumerate(content):
    if i == 175:
        print(line)
"""

"""
page = "https://www.kursna-lista.com/kursne-liste-banaka-i-menjacnica"
GetPage = requests.get(page)
GetPageContent = GetPage.content
with open("D:\Python\Blablabla\TestFairu2.html",'w+') as WriteFile:
    WriteFile.write(str(GetPageContent))
"""
