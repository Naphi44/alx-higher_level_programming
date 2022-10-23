#!/usr/bin/python3
"""
    This takes in a letter and sends a POST request to
    a given URL, using the letter as a parameter
"""
import requests
from sys import argv

if __name__ == "__main__":
    letter = argv[1] if len(argv) > 1 else ""
    post_data = {'q': letter}

    url, data = "http://0.0.0.0:5000/search_user", post_data
    r = requests.post(url, data)

    try:
        dic = r.json()
        if dic:
            print("[{}] {}".format(dic.get("id"), dic.get("name")))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
