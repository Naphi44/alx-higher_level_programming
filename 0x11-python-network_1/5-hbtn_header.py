#!/usr/bin/python3
"""
    This script takes a URL, sends a request
    and displays the X-Request-Id
"""

import requests
from sys import argv

if __name__ == "__main__":
    with requests.get(argv[1]) as response:
        print(response.headers.get("X-Request-Id"))
