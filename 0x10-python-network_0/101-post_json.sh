#!/usr/bin/env bash
# Script to send a POST request with json data from a file

if [ $# -gt 1 ]; then
	curl -sX POST -H 'Content-Type: application/json' -d "@$2" "$1"
fi
