#!/bin/bash
#sends a DELETE request to the URL passed as the first argv.
curl -sX DELETE "$1"
