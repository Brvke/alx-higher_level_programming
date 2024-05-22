#!/usr/bin/python3
""" takes url argument and returns X-Request-Id value of header"""
import sys
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1]

    reqs = urllib.request.Request(url)

    with urllib.request.urlopen(reqs) as response:
        headers = response.info()
        x_request_id = headers.get('X-Request-Id')
