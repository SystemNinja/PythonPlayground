#This program demonstrates a process called webscraping, what this does is simply pull a certain data or info from a web page(precisely its html file)
#This example uses Beautiful Soup library as well as requests
#pip install requests, pip install beautifulsoup4 ,bs4 is the latest version of library
#site: http://pythonhow.com/example.html

#NOTE: GO THROUGH ALL FUNCTIONS OF Beautiful Soup and requests functions in separate program.

import requests
from bs4 import BeautifulSoup

#load source code of web page into variable r
r = requests.get("http://pythonhow.com/example.html")
#grab content from request data type
c = r.content
#print(c)
#check for other parsers(2nd argument)
#if soup is printed it will return source code of a web page that is properly sorted line by line, not messy
soup=BeautifulSoup(c,"html.parser")
#print(soup)

#following line will extract all div elements which contain class cities which will be passed as dictionary
all=soup.find("div",{"class":"cities"})
print(all)


#as the word says, find all will return all elements taht contain class cities, that information will be passed as dictionary
all=soup.find_all("div",{"class":"cities"})
#print(all[1]) #prints second element in the list
print(all[2].find_all("h2"))#prints third element that is located under the h2 tags only
#[0].text, is indexing, .text means just to return value as text
print(all[2].find_all("h2")[0].text)#prints the text only without tags
print(all[2].find("h2").text)#this approach uses find insteand of find_all which nullifies the need to use indexing after h2 tag

print("\nsome distinction here\n")
#printing out all city names
for item in all:
    print(item.find("h2").text)
    print(item.find("p").text)#return content from p tag
