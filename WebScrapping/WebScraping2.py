"""
This program demonstrates webscraping a real estate website.

Reference:
https://www.udemy.com/the-python-mega-course/learn/v4/t/lecture/5565484?start=0 

Site source:
https://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/ 
"""

import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/ ")
c = r.content #Get content of requests object r
soup = BeautifulSoup(c, "html.parser")

all=soup.find_all("div", {"class":"propertyRow"})
#[0] determines which h4 element will be choosen, like first and second 
# \n is replaced with empty string even tho it is not visible physically, it will make empty row above and below price if left untouched
print(all[0].find("h4", {"class":"propPrice"}).text.replace("\n","")) 
