#!/bin/bash
# takes in a URL, sends a delete request to the URL, and displays the body
curl -X DELETE "$1"
