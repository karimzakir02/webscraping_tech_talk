import json
import requests
import ssl
import urllib3
from selenium import webdriver
urllib3.disable_warnings()
ssl._create_default_https_context = ssl._create_unverified_context

headers = {"x-apikey": "1im1hL52q9xvta16GlSdYDsTsG0dmyhF"}

json_args = {
    "pagination": {
        "from": 0,
        "size": 48
    },
    "banner": "loblaw",
    "cartId": "c4f214ee-a938-4f35-873b-1e9073804b3e",
    "lang": "en",
    "date": "25072022",
    "storeId": "1000",
    "pcId": None,
    "pickupType": "STORE",
    "offerType": "ALL"
}

response = requests.post(
    "https://api.pcexpress.ca/product-facade/v3/products/deals", headers=headers, json=json_args, 
    verify=False)

print(response.json()["results"][0])