"""
    Script for a quick table retrieval from the F1 website
    https://www.formula1.com/en/results.html
"""
import pandas as pd
import requests

fav_race = "placeholder"
response = requests.get(fav_race)

# Two ways:
direct_table = pd.read_html(fav_race)  # direct

if response.status_code == 200:
    requests_table = requests.get(response.text)  # through requests text

print(direct_table)
