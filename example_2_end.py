import requests
from bs4 import BeautifulSoup
import ssl
import urllib3
urllib3.disable_warnings()
ssl._create_default_https_context = ssl._create_unverified_context

link = "https://www.formula1.com/en.html"

response = requests.get(link, verify=False)
response.encoding = "gzip"

soup = BeautifulSoup(response.text, features="lxml")

blocks = soup.find_all(attrs={"class": "f1-cc--caption"})

for block in blocks:
    title = block.find(attrs={"class": "no-margin"})
    if title:
        print(title.get_text())
