#!/usr/bin/python3
'''
Script that fetches a website
'''
import requests
import sys

if __name__ == "__main__":
    link = sys.argv[1]
    url = requests.get(link)
    print(url.headers.get)
