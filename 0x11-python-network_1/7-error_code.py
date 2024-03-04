#!/usr/bin/python3
'''
That takes in a URL, sends a request to a URL
then displays the body of the response
'''
import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    stat_code = response.status_code
    if stat_code > 400:
        print('Error code: {}'.format(stat_code))
    else:
        print('{}'.format(response.text))
