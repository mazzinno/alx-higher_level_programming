#!/usr/bin/python3
'''task 6'''

if __name__ == "__main__":
    import requests
    import sys
    data = {'email': sys.argv[2]}
    response = requests.post(sys.argv[1], data)
    print(response.text)
