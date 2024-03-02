#!/bin/bash
# display all HTTP methods the server will accept.
curl -sI "$1" | grep -i Allow: | cut -c 8-
