from packages import Packages
from src.package_manager import PackageManager


CONFIG_MAP = {
    # bspwm + sxhkd
    "bspwm/bspwmrc": "~/.config/bspwm/bspwmrc",
    "sxhkd/sxhkdrc": "~/.config/sxhkd/sxhkdrc",


    # Панель и уведомления
    "polybar/config.ini": "~/.config/polybar/config.ini",
    "polybar/launch.sh": "~/.config/polybar/launch.sh",
    "dunst/dunstrc": "~/.config/dunst/dunstrc",
    "picom/picom.conf": "~/.config/picom/picom.conf",


    # Rofi
    "rofi/config.rasi": "~/.config/rofi/config.rasi",
    "rofi/themes/": "~/.config/rofi/themes/",  # если папка

    # X11
    "x11/xinitrc": "~/.xinitrc",

    # GTK / темы
    "gtk-3.0/settings.ini": "~/.config/gtk-3.0/settings.ini",
    "lxappearance/lxappearance.conf": "~/.config/lxappearance/lxappearance.conf",

    # Betterlockscreen
    "betterlockscreen/betterlockscreenrc": "~/.config/betterlockscreen/betterlockscreenrc",
}

TO_INSTALL = (
        Packages.base +
        Packages.desktop +
        Packages.session +
        Packages.network +
        Packages.sound +
        Packages.bluetooth +
        Packages.fonts +
        Packages.system +
        Packages.storage +
        Packages.apps +
        Packages.games +
        Packages.gnome_essential_for_wm
)

pm = PackageManager(aur_helper="yay")

# Установка зависимостей
pm.install_package(TO_INSTALL)

#


