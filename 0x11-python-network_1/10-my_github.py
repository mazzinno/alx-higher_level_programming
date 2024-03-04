#!/usr/bin/python3
'''task 10'''

if __name__ == "__main__":
    import requests
    import sys
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    info = (username, password)
    response = requests.get(url, auth=info)
    print('Body response:')
    try:
        print(response.json()['id'])
    except Exception:
        print('None')
