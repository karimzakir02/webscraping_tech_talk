import json
import requests
import certifi
import ssl
import urllib3
from selenium import webdriver
urllib3.disable_warnings()
ssl._create_default_https_context = ssl._create_unverified_context

link = "https://api.pcexpress.ca/product-facade/v3/products/deals"

json_payload = {
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
    "offerType": "ALL",
    "filter": {
        "categories": ["27985"],
        "promotions": ["Price Reduction"]
    }
}

response = requests.post(link,
                         json=json_payload,
                         verify=False)
print(response.status_code)
# .json()["results"]
