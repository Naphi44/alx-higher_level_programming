#!/usr/bin/python3
"""
    This script takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""
import requests
from sys import argv

if __name__ == "__main__":
    username, passwd = argv[1], argv[2]
    url = "https://api.github.com/user"

    r = requests.get(url, auth=(username, passwd))

    if r.status_code >= 400:
        print(None)
    else:
        try:
            dic = r.json()
            if dic:
                print("{}".format(dic.get("id")))
            else:
                print(None)
        except Exception:
            print(None)
