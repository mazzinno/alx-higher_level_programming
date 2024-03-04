#!/usr/bin/python3
'''
Script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)
'''

if __name__ == "__main__":
    import urllib.request
    import sys
    try:
        url = sys.argv[1]
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as r:
            response = r.read()
            print(response.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')
