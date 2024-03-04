#!/usr/bin/python3
'''
Takes in a URL, sends a request to the URL and displays the value of
variable X-Request-Id in the response header
'''

if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
