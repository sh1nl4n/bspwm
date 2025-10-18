
from src.dotfile_manager import DotfileManager
from pathlib import Path
import subprocess
import os

# === 2. Развёртывание конфигов ===
print("\n⚙️  Развёртывание конфигурационных файлов...")
dm = DotfileManager(dotfiles_dir="./dotfiles")  # или "~/dotfiles", если храните там

CONFIG_MAP = {
     # bspwm + sxhkd
    "bspwm/bspwmrc": "/home/snake/.config/bspwm/bspwmrc",
    "sxhkd/sxhkdrc": "/home/snake/.config/sxhkd/sxhkdrc",


    # Панель и уведомления
    "polybar/": "/home/snake/.config/polybar/",
    "dunst/dunstrc": "/home/snake/.config/dunst/dunstrc",
    "picom/picom.conf": "/home/snake/.config/picom/picom.conf",


    # Rofi
    "rofi/": "/home/snake/.config/rofi/",


    # X11
    "x11/xinitrc": "/home/snake/.xinitrc",


    # GTK / темы
    "gtk-3.0/settings.ini": "/home/snake/.config/gtk-3.0/settings.ini",


    # Betterlockscreen
    "betterlockscreen/betterlockscreenrc": "/home/snake/.config/betterlockscreen/betterlockscreenrc",


    # Themes
    "fonts/": "/home/snake/.local/share/fonts/local/",
    "themes/": "/home/snake/.themes/",
    "icons/": "/home/snake/.icons/",

    # Other
    "pictures/": "/home/snake/Pictures/",
    "bin/": "/home/snake/bin/",
    "autorandr": "/home/snake/.config/autorandr",
    "etc/logind.conf": "/etc/systemd/logind.conf",
    "x11/00-keyboard.conf": "/etc/X11/xorg.conf.d/00-keyboard.conf",
    "x11/50-touchpad.conf": "/etc/X11/xorg.conf.d/50-touchpad.conf",
    "micro/": "/home/snake/.config/micro/",
    "alacritty/": "/home/snake/.config/alacritty/"
}

dm.deploy_configs(CONFIG_MAP)



# === 3. Пост-установка: права и инициализация ===
print("\n🔧 Пост-установка...")

subprocess.run(["sudo", "usermod", "-aG", "docker", "$USER"], stdout=subprocess.DEVNULL, check=True)

executables = [
    "/home/snake/.config/bspwm/bspwmrc",
    "/home/snake/.config/sxhkd/sxhkdrc",
    "/home/snake/.config/polybar/launch.sh",
    "/home/snake/.config/autorandr/postswitch",
    "/home/snake/.xinitrc",
    "/home/snake/bin/lock_screen.sh",
    "/home/snake/bin/color_pick.sh",
]

for path_str in executables:
    path = Path(os.path.expanduser(path_str))
    if path.exists():
        path.chmod(0o777)
        print(f"✅ Сделан исполняемым: {path}")

# Инициализация betterlockscreen (если используется)
if "betterlockscreen" in to_install:
    try:
        subprocess.run(["betterlockscreen", "-u", "~/pictures/wallpaper.jpg"], check=False)
        print("🖼️  Betterlockscreen: обои установлены")
    except Exception as e:
        print(f"⚠️  Не удалось инициализировать betterlockscreen: {e}")

print("\n🎉 Готово! Перезапустите сессию или выполните: startx")