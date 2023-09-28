#!/bin/bash
# script that makes a request to 0.0.0.0:5000/catch_me to server to respond
curl -sL -X PUT -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
