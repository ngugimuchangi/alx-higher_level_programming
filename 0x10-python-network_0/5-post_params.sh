#!/usr/bin/env bash
# Script to send a POST request with specific data

if [ $# -gt 0 ]; then
	curl -sX POST -d "email=test@gmail.com&subject=I+will+always+be+here+for+PLD" "$1"
fi
