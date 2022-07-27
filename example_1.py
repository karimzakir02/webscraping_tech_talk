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

fav_race = "https://www.formula1.com/en/results.html/2022/races/1116/france/race-result.html"
response = requests.get(fav_race, verify=False)

# Two ways:
direct_table = pd.read_html(fav_race)

# Or:
# if response.status_code == 200:
#     requests_table = pd.read_html(response.content)[0]  # through requests text

print(direct_table)
