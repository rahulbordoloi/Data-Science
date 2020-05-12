#Beautiful Soup
"""in web dev, the term 'tap soup' refers to structurally or syntactically incorrect HTML Code written for a webpage"""

from bs4 import BeautifulSoup
import requests

url="https://rahulbordoloi.github.io/"
r = requests.get(url)
html_doc = r.text

#create BS object from resulting HTML and pretify it .
soup = BeautifulSoup(html_doc)
print(soup.prettify())

#to get the title
print(soup.title)

#to get the text
print(soup.get_text())

#find all 'a' tags (which define hyperlinks)
a_tags = soup.find_all('a')

#variable a_tags is a ResultSet
for link in a_tags:
    print(link.get('href'))