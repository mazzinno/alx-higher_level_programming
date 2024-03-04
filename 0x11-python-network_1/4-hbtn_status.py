#!/usr/bin/python3
'''
Script that fetches a website
'''
import requests

if __name__ == "__main__":
    url = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(url.text)))
    print('\t- content: {}'.format(url.text))
