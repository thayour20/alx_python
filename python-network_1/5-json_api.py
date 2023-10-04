#!/bin/usr/python

import requests
import sys

if len(sys.argv) == 2:
    lether = sys.argv[1]

else:
    lether =""

url = 'http://0.0.0.0:5000/search_user'
payload = {'q':lether}


response = requests.post(url, data = payload)

try:
    data = response.json()
    if data:
        print("[{}] {}".format(data['id'], data['name']))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
