import requests
from bs4 import BeautifulSoup

link = "https://www.formula1.com/en.html"

response = requests.get(link)
response.encoding = "gzip"

soup = BeautifulSoup(response.text, features="lxml")

# Also use the primitive approach

blocks = soup.find_all(attrs={"class": "f1-cc--caption"})

for block in blocks:
    title = block.find(attrs={"class": "no-margin"})
    if title:
        print(title.get_text())
