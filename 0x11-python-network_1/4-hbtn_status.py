#!/usr/bin/python3
'''
Script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)
'''

if __name__ == "__main__":
    import requests
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(r)))
    print('\t- content: {}'.format(r.text))
