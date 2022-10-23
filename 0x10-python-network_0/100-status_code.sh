#!/bin/bash
# Script that display the status code of a HTTP response
curl -so /dev/null -w '%{http_code}' "$1"
