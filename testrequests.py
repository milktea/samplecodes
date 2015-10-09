#Using Python with the Internet
#Python requests, parsing xml, beautifulsoup
#Return article links from thoughtcatalog.com
#Milktea

import requests
from bs4 import BeautifulSoup

result = requests.get('http://thoughtcatalog.com')

#print result.status_code
#print result.headers

data = result.text
soup = BeautifulSoup(data, 'html.parser')
for item in soup.find_all('article', {'class': 'type-post'}):
    a = item.find_all('a')[1]
    print a.attrs['href']

#print soup
#print result
