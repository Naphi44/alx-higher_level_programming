#!/usr/bin/python3
"""
    Sends a POST request with an email as parameter and
    displays the body of the response
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    data = {"email": argv[2]}
    with requests.post(url, data) as response:
        print(response.text)
