#!/bin/bash
# Script that send adds a custom request header to a GET request
curl -sH "X-School-User-Id: 98" "$1"
