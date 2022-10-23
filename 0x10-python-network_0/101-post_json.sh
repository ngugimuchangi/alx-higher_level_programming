#!/bin/bash
# Script to send a POST request with json data from a file
curl -sX POST -H 'Content-Type: application/json' -d "@$2" "$1"
