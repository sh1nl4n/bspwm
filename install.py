from packages import Packages
from src.package_manager import PackageManager
from src.dotfile_manager import DotfileManager
from pathlib import Path
import subprocess
import os



# === 1. Установка пакетов ===
pm = PackageManager(aur_helper="yay")

to_install = (
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

print("📥 Установка пакетов...")
pm.install_packages(to_install)



# === 2. Развёртывание конфигов ===
print("\n⚙️  Развёртывание конфигурационных файлов...")
dm = DotfileManager(dotfiles_dir="./dotfiles")  # или "~/dotfiles", если храните там

CONFIG_MAP = {
     # bspwm + sxhkd
    "bspwm/bspwmrc": "~/.config/bspwm/bspwmrc",
    "sxhkd/sxhkdrc": "~/.config/sxhkd/sxhkdrc",


    # Панель и уведомления
    "polybar/": "~/.config/polybar/",
    "dunst/dunstrc": "~/.config/dunst/dunstrc",
    "picom/picom.conf": "~/.config/picom/picom.conf",


    # Rofi
    "rofi/": "~/.config/rofi/",


    # X11
    "x11/xinitrc": "~/.xinitrc",


    # GTK / темы
    "gtk-3.0/settings.ini": "~/.config/gtk-3.0/settings.ini",


    # Betterlockscreen
    "betterlockscreen/betterlockscreenrc": "~/.config/betterlockscreen/betterlockscreenrc",


    # Themes
    "fonts/": "~/.local/share/fonts/local/",
    "themes/": "~/.themes/",
    "icons/": "~/.icons/",

    # Other
    "pictures/": "~/Pictures/",
    "bin/": "~/bin/",
    "autorandr": "~/.config/autorandr",
    "etc/logind.conf": "/etc/systemd/logind.conf",
    "x11/00-keyboard.conf": "/etc/X11/xorg.conf.d/00-keyboard.conf",
    "x11/50-touchpad.conf": "/etc/X11/xorg.conf.d/50-touchpad.conf",
    "micro/": "~/.config/micro/",
    "alacritty/": "~/.config/alacritty/"
}

dm.deploy_configs(CONFIG_MAP)



# === 3. Пост-установка: права и инициализация ===
print("\n🔧 Пост-установка...")

subprocess.run(["sudo", "usermod", "-aG", "docker", "$USER"], stdout=subprocess.DEVNULL, check=True)

executables = [
    "~/.config/bspwm/bspwmrc",
    "~/.config/sxhkd/sxhkdrc",
    "~/.config/polybar/launch.sh",
    "~/.config/autorandr/postswitch",
    "~/.xinitrc",
    "~/bin/lock_screen.sh",
    "~/bin/color_pick.sh",
]

for path_str in executables:
    path = Path(os.path.expanduser(path_str))
    if path.exists():
        path.chmod(0o755)
        print(f"✅ Сделан исполняемым: {path}")

# Инициализация betterlockscreen (если используется)
if "betterlockscreen" in to_install:
    try:
        subprocess.run(["betterlockscreen", "-u", "~/pictures/wallpaper.jpg"], check=False)
        print("🖼️  Betterlockscreen: обои установлены")
    except Exception as e:
        print(f"⚠️  Не удалось инициализировать betterlockscreen: {e}")

print("\n🎉 Готово! Перезапустите сессию или выполните: startx")