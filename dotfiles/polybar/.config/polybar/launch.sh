#!/usr/bin/env bash

pkill polybar && sleep 1

export PRIMARY_MONITOR=$(xrandr --query | awk '/ primary/ {print $1; exit}')

PRIMARY_MONITOR="$PRIMARY_MONITOR" polybar  -c ~/.config/polybar/config.ini   &
