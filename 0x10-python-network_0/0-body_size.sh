#!/bin/bash
# displays the size of the body of response.
curl -sI "$1" | grep 'Content-Length:' | cut -c 17-
