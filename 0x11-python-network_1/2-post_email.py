#!/usr/bin/python3
""" send a post to url and print reply """
import sys
import urllib.request


if __name__ == '__main__':
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values).encode('ascii')
    with urllib.request.urlopen(sys.argv[1], data=data) as response:
        body = response.read().decode('utf-8')
        print(body)
