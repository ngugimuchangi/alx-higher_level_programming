#!/bin/bash
# Script to send a PUT request and cause server to respond with a the message 'You got me!'
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
