from packages import Packages
from src.package_manager import PackageManager


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