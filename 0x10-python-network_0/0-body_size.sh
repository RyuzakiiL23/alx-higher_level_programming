#!/bin/bash
# script that takes in a URL, sends a request to URL displays size of the body

curl -s "$1" | wc -c
