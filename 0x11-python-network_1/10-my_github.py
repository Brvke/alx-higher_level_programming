#!/usr/bin/python3
'''Python script to take github credentials and
display github id'''

if __name__ == "__main__":
    import requests
    import sys

    username = sys.argv[1]
    passw = sys.argv[2]
    headers = {"Authorization": f"Bearer {pat}"}
    response = requests.get(
        f"https://api.github.com/users/{username}",
        headers=headers)
    if response.status_code == 200:
        print(f"Your GitHub ID: {response.json(['id'])}")
    else:
        print(f"Error: HTTP status code {response.status_code}")
