#!/usr/bin/python3
'''task 2'''

if __name__ == '__main__':
    import urllib.request
    import urllib.error
    import sys
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        info = response.read()
    print(info.decode("ascii"))
