#!/usr/bin/bash
# Script that sends a DELETE request to a server

if [ $# -gt 0 ]; then
	curl -sX DELETE "$1"
fi
