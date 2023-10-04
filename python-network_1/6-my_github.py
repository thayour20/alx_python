#!/bin/usr/python

import requests
import sys


username = sys.argv[1]
password = sys.argv[2]
authentification = (username, password)

url = "https://api.github.com/user"

response = requests.get(url, auth = authentification)

if response.status_code // 100 == 2:
    data = response.json()

    print(data["id"])
else:
    print("None")