#!/bin/python

import requests
from bs4 import BeautifulSoup

f = open("index.html", "a")

baseurl = 'https://www.skysports.com/euro-2020-fixtures'
html_page = requests.get(baseurl).text
soup = BeautifulSoup(html_page,'html.parser')

f.write("<html><head><title>EURO FIXTURES</title></head><body>")

for a in soup.find_all('div','fixres__item'):
    team1=a.find('span','matches__participant--side1').find(attrs={'class':'swap-text__target'} )
    team2=a.find('span','matches__participant--side2').find(attrs={'class':'swap-text__target'} )
    f.write(team1.text+" vs "+team2.text+"\n")
    
f.write("</body></html>")
f.close()


   




