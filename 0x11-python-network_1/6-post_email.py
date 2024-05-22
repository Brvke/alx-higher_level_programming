#!/usr/bin/python3
"""script to post to a url with email"""
import requests
import sys


if __name__ == '__main__':
    response = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(response.text)
