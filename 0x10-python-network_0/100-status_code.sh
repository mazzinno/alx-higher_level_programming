#!/bin/bash
#Sends a request to a URL passed as an argument.
curl -so /dev/null -w "%{http_code}" "$1"
