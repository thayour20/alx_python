#!/bin/usr/python

import requests
import sys

if len(sys.argv) != 2:
    print("Usage: ./4-error_code.py <url>")
    sys.exit(1)

url = sys.argv[1]

response = requests.get(url)

print(response.text)

#if response.status_code <= 400:

