#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

from i3pystatus import Status

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
white       = "#f1edfb"
darkwhite   = "#f1edfb"
background  = "#133B47"

status = Status(standalone=True)

status.register("clock",
    format=" %a %-d %b %X",)

status.register("battery",
    format="{status} {percentage:.0f}% {remaining:%E%h:%M}",
    alert=True,
    alert_percentage=15,
    color=white,
    critical_color=red,
    charging_color=yellow,
    full_color=white,
    status={
        "DIS": "",
        "CHR": "",
        "FULL": "",
    },)

status.register("pulseaudio",
    format=" {volume}%",
    color_muted=red,
    color_unmuted=white,)

status.register("network",
    interface="wlp6s0",
    color_up=white,
    color_down=red,
    format_up=" {essid} {quality:.0f}%",)

status.run()
