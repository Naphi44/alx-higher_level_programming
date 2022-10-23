#!/usr/bin/python3
"""This script takes a URL, sends a request
and displays the X-Request-Id"""

from urllib.request import urlopen
from sys import argv

if __name__ == "__main__":
    with urlopen(argv[1]) as response:
        body = response.read()
        print(response.getheader("X-Request-Id"))
