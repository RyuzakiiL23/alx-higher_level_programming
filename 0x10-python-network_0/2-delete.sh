#!/bin/bash
# takes in a URL, sends a delete request to the URL, and displays the body
curl -sX DELETE "$1"
