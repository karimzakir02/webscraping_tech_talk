import requests
from bs4 import BeautifulSoup  # pip install beautifulsoup4
import ssl
import urllib3
urllib3.disable_warnings()
ssl._create_default_https_context = ssl._create_unverified_context

link = "https://www.formula1.com/en.html"

response = requests.get(link, verify=False)
response.encoding = "gzip"

soup = BeautifulSoup(response.text, features="lxml")

# Matches using OR
blocks = soup.find_all(attrs={"class": ["f1--s", "no-margin"]})

for block in blocks:
    print(block.text)
