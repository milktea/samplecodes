#Using Python with the Internet
#MySQL database with Python
#Saves article links from thoughtcatalog.com into MySQL Database
#Milktea

import requests
from bs4 import BeautifulSoup
from dbconnect import connection
import time

result = requests.get('http://thoughtcatalog.com')
soup = BeautifulSoup(result.text, 'html.parser')
c, conn = connection()

def parse_links():
    for item in soup.find_all('article',{'class': 'type-post'}):
        a = item.find_all('a')[0]
        url = a.attrs['href']
	c.execute("SELECT * FROM links WHERE link = (%s)",([url]))	
	rows = c.fetchall()

	if len(rows)==0:
       	    c.execute("INSERT INTO links (time, link) VALUES (%s, %s)",
			(time.time(), url))
            conn.commit()
	    print("Found a new link!")
	else:
	    print(rows)
	    print("Link already in database")
	time.sleep(5)  
    conn.close()

while True:
    parse_links()
#print result.status_code
#print result.headers
#print soup
#print result
