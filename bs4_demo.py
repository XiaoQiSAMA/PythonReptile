import requests
import re
from bs4 import BeautifulSoup

url = "http://python123.io/ws/demo.html"
demo = requests.get(url).text
soup = BeautifulSoup(demo, "html.parser")
#print(soup.title)
#print(soup.a)
#print(soup.prettify())

for link in soup.find_all('a'):
    print(link.get('href'))

f = soup.find_all(string = re.compile("python"))
print(f)