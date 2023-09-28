#!/bin/bash
# script that isplays the body of the response.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
