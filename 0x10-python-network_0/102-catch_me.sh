#!/bin/bash
# Script to send a PUT request with data to append to a file
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
