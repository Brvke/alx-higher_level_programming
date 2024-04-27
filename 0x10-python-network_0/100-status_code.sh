#!/bin/bash
# Bash script that sends a request and displas status code
curl -s -o /dev/null -w "%{http_code}" "$1"
