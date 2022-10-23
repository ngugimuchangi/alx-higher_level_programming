#!/bin/bash
# Script that displays all HTTP methods a server will accept
curl -sIX OPTIONS "$1" | grep Allow | cut -d ' ' -f 2-
