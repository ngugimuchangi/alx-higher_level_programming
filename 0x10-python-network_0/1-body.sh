#!/usr/bin/env bash
# Script to send a GET request and display the response

if [ $# -gt 0 ]; then
	if curl -sI "$1" | grep -q 200; then
		curl -s "$1"
	fi
fi
