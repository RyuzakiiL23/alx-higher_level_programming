#!/bin/bash
# script that send a head request and extract all HTTP methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
