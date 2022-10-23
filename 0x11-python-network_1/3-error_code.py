#!/usr/bin/python3
"""
    This script sends a request to the URL and displays the body of the
    response handling error appropriately
"""
from urllib import request, error
from sys import argv

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode("utf8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
