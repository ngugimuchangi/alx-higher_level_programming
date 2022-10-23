#!/usr/bin/env bash
# Script that display the status code of a HTTP response

if [ $# -gt 0 ]; then
	curl -so /dev/null -w '%{http_code}' "$1"
fi
