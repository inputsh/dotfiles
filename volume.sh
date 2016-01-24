#!/bin/bash

volume=$(awk -F"[][]" '/dB/ { print $2 }' <(amixer sget Master))
playback=$(amixer sget Master | grep 'Mono:\ Playback' | awk '{ print $6 }')

if [ "$playback" == "[on]" ]; then
    icon=""
    echo $icon $volume
else
    icon=" M"
    echo $icon
fi
