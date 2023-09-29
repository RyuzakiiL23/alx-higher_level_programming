#!/usr/bin/python3
"""Python script that fetches"""

import urllib.request
if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as f:
        r = f.read()
    print('Body response:')
    print('\t- type: {}'.format(type(r)))
    print('\t- content: {}'.format(r))
    print('\t- utf8 content: {}'.format(r.decode('utf-8')))
