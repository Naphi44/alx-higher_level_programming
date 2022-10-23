#!/usr/bin/python3
"""
    This script sends a request to the URL and displays the body of the
    response handling error appropriately
"""
import requests
from sys import argv

if __name__ == "__main__":
    with requests.get(argv[1]) as response:
        if response.status_code >= 400:
            print("Error code: {}".format(response.status_code))
        else:
            print(response.text)
