#!/bin/usr/python

import requests
import sys

   
url = 'https://api.github.com/user'
username = sys.argv[1]
password = sys.argv[2]
authentification = (username, password)

response = requests.get(url, data = authentification)

if response.status.code // 100 == 2:
    data = response.jason()

    print(data["id"])
else:
    print("None")