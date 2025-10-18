#!/usr/bin/env bash

pkill polybar && sleep 1
polybar -c ~/.config/polybar/config.ini &

