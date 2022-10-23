#!/usr/bin/bash
# Script that displays all HTTP methods a server will accept

if [ $# -gt 0 ]; then
	curl -sIX OPTIONS "$1" | grep Allow | cut -d ' ' -f 2-
fi
