#!/usr/bin/python3
"""Sends a POST request with an email as parameter and
displays the body of the response"""
from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    data = parse.urlencode(value)
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print(response.read().decode("utf8"))
