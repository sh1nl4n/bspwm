#!/bin/env bash

# choice=$(printf "Lock\nLogout\nSuspend\nReboot\nShutdown" | rofi -dmenu)
# case "$choice" in
#   Lock) $HOME/bin/lock_screen.sh ;;
#   Logout) pkill -KILL -u "$USER" ;;
#   Suspend) systemctl suspend && $HOME/bin/lock_screen.sh ;;
#   Reboot) systemctl reboot ;;
#   Shutdown) systemctl poweroff ;;
# esac


#! /bin/sh

rofi_cmd() {
	rofi -dmenu \
		-theme ~/.config/rofi/powermenu.rasi
}

chosen=$(printf "poweroff\nreboot\nlock\nsuspend\nlogout" | rofi_cmd)

case "$chosen" in

	"poweroff") poweroff ;;
	"reboot") reboot ;;
  "lock") $HOME/bin/lock_screen.sh ;;
  "suspend") systemctl suspend && $HOME/bin/lock_screen.sh ;;
	"logout") pkill -KILL -u "$USER" ;;
	*) exit 1 ;;

esac
