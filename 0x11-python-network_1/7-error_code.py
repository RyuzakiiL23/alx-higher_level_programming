#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8)."""

import requests
import sys
if __name__ == "__main__":
    try:
        with requests.get(sys.argv[1]) as res:
            res.raise_for_status()
            print(res.text)
    except requests.exceptions.RequestException as err:
        print('Error code:', str(err))
