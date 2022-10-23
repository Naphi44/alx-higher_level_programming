#!/bin/bash
# This script displays the size of the body of a URL response
curl -sI "$1" | grep "Content-Length" | cut -d " " -f 2
