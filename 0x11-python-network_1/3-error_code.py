#!/usr/bin/python3
""" send s request and prints response body while managing error """
import urllib.request
import sys
import urllib.error


if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf8'))
    except urllib.error.HTTPError as err:
        print(f'Error code: {err.code}')
