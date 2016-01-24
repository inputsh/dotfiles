#!/bin/bash

something=$(curl -s https://api.github.com/notifications\?access_token\={{ YOUR TOKEN GOES HERE }} \
    | grep "unread" \
    | wc -l)

echo "" $something
