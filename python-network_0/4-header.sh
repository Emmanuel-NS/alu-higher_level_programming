#!/bin/bash
# Script that sends GET request for route validation with header parameter
#curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
curl -sH "X-HolbertonSchool-User-Id: 98" "${1}"
