#!/bin/bash
# Bash script that sends a JSON POST request
curl -s -X POST -H 'Content-Type: application/json' -d "@$2" "$1"
