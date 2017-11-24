#!/bin/bash

color="#FDC882"

# show charging icon if the laptop is charging
charging=$(acpi -V | grep -Eo 'Adapter\ 0:\ on-line')
if [ -n "$charging" ]; then
    echo  AC
fi

# get remaining battery time
remaining=$(acpi -V | grep -o [0-9][0-9]:[0-9][0-9])

echo  $remaining
