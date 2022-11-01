#Use of this program is used as test environment on ways how to pull data from web(webscraping) for euro course specifically

import requests
from bs4 import BeautifulSoup

#This method pulls euro course in RSD from specified web page and returns it as float, returned value can be used to peform various calculations
def pullCourse():
    page = "https://www.kursna-lista.com"
    #Establishing "connection" with the page or more like loading page into memory
    r = requests.get(page)
    #Grabing content of the page in form of HTML code
    c = r.content
    #Parsing the content of the web page using BeatuifulSoup and its html parser, this will actually sort the content and make html code be in its own respective line
    soup = BeautifulSoup(c,"html.parser")
    #The required info is located under the div with class=boxContent, since page has multiple elements with same class, we are going to go through all of them and select
    #the one which holds data we want
    course_box = soup.find_all("div", {"class":"boxContent"})
    #By manually searching the page source, it was discovered that second div is in question therefore it will be selected by index [1], under that div, 
    #required data is located under the first <td> tag, using .text, data is isolated from html tags as string number. 
    #find() is used instead of find_all() because there is no need to go through other <td> tags therefore additional indexing is not required as well. 
    course_data = course_box[1].find("td").text
    return float(course_data)

#euro = float(input("Enter euros:"))
euro = 10
print("Course:",pullCourse())#Printing initial course
print(pullCourse()*euro)