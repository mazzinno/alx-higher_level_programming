#!/usr/bin/python3
'''task 6'''

if __name__ == "__main__":
    import requests
    import sys
    if len(sys.argv) != 1:
        data = {'q': sys.argv[1]}
    else:
        data = {'q': ""}
    response = requests.post('http://0.0.0.0:5000/search_user', data)
    try:
        # Try to parse the response as JSON
        json_data = response.json()
        if not json_data:
            print('No result')
        else:
            user_name = json_data['name']
            user_id = json_data['id']
            print('[{}] {}'.format(user_id, user_name))
    except ValueError:
        # Print an error message if parsing fails
        print('Not a valid JSON')
