#!/usr/bin/python3
'''task 0'''

if __name__ == "__main__":
    import urllib.request
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as r:
        response = r.read()
        print('Body response:')
        print(f'\t- type: {type(response)}')
        print(f'\t- content: {response}')
        print(f'\t- utf8 content: {response.decode("utf-8")}')
