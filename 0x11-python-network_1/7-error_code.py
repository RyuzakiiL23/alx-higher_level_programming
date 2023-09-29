#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8)."""

import requests
import sys
if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r == 200:
        print(res.text)
    else:
        print('Error code:', err.text)
