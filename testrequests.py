#Using Python with the Internet
#Python requests, parsing xml, beautifulsoup
#Return article links from thoughtcatalog.com
#Milktea

import requests
from bs4 import BeautifulSoup

result = requests.get('http://thoughtcatalog.com')
soup = BeautifulSoup(result.text, 'html.parser')
for item in soup.find_all('article',{'class': 'type-post'}):
    a = item.find_all('a')[1]
    print a.attrs['href']

#print result.status_code
#print result.headers
#print soup
#print result
