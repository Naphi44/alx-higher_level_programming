#!/usr/bin/python3
"""Script that fetches a URL"""
import requests

if __name__ == "__main__":
    with requests.get("https://alx-intranet.hbtn.io/status") as response:
        body = response.text

        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
