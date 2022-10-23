#!/bin/bash
# Script that send adds a custom request header to a GET request

if [ $# -gt 0 ]; then
	curl -sH "X-School-User-Id: 98" "$1"
fi
