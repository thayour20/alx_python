#!/bin/usr/python3
import requests
import sys

if len(sys.argv) != 2:
    print ("Usage: ./1-hbtn_header.py <URL>")

url = sys.argv[1]

response = requests.get(url)

if 'X-Request-Id' in response.headers:
    print( response.headers['x-Request-Id'])
