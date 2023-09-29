#!/usr/bin/python3
"""Python script that displays the value of the X-Request-Id"""

import urllib.request
import sys
if __name__ == "__main__":

    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as f:
        print(dict(f.headers).get("X-Request-Id"))
