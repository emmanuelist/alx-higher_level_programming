#!/bin/bash
# cURL only method
curl -sI "$1" | grep Allow | cut -d ' ' -f2-
