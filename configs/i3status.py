#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

from i3pystatus import Status
from i3pystatus.weather import wunderground

black       = "#2c2836"
darkblack   = "#73707e"
red         = "#bb7473"
darkred     = "#cf9fa4"
green       = "#68b782"
darkgreen   = "#9acbad"
yellow      = "#abb773"
darkyellow  = "#c5cba4"
blue        = "#7865c5"
darkblue    = "#a396d9"
magenta     = "#bb65b6"
darkmagenta = "#cf96cf"
cyan        = "#68a8c5"
darkcyan    = "#9ac1d9"
white       = "#a7adba"
greenish    = "#aaccbb"
darkwhite   = "#bbaacc"
background  = "#133B47"

status = Status(standalone=True)

status.register("clock",
    format=" %a %-d %b %X",
    color=white)

status.register("battery",
    format="{status} {percentage:.0f}% {remaining:%E%h:%M}",
    alert=True,
    alert_percentage=15,
    color=white,
    critical_color=red,
    charging_color=greenish,
    full_color=white,
    status={
        "DIS": "",
        "CHR": "",
        "FULL": "",
    },)

status.register('weather',
    format='{icon}[ {current_temp}{temp_unit}]',
    color=white,
    backend=wunderground.Wunderground(
        api_key='',
        location_code='zmw:00000.1.14654',
        units='metric',
    ),)

status.register('github',
    access_token='',
    format=" {unread_count}",
    color=white)

status.register("pulseaudio",
    format=" {volume}%",
    color_muted=red,
    color_unmuted=white,)

status.run()
