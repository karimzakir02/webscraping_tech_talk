"""
    Script for a quick table retrieval from the F1 website
    https://www.formula1.com/en/results.html
"""
import pandas as pd
import requests
import ssl
import urllib3 
urllib3.disable_warnings()
# Not necessary, my laptop doesn't have SSL verification, but it's not prod, so:
ssl._create_default_https_context = ssl._create_unverified_context

standings = "https://www.formula1.com/en/results.html/2023/drivers.html"
direct_table = pd.read_html(standings)

# Second way of scraping:
response = requests.get(standings, verify=False)


# Or:
# if response.status_code == 200:
#     requests_table = pd.read_html(response.content)[0]  # through requests text

print(direct_table)
