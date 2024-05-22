#!/usr/bin/python3
'''Python script that takes a leter and posts'''

if __name__ == "__main__":
    import requests
    import sys

    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]

    response = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})

    response_json = response.json()
    if response_json == {}:
        print("No result")
    elif response_json.get("id") is None or response_json.get("name") is None:
        print("Not a valid JSON")
    else:
        print(f"[{response_json.get('id')}] {response_json.get('name')}")
