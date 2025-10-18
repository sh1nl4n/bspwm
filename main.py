from src.dotfile_manager import DotfileManager

dm = DotfileManager(dotfiles_dir="./dotfiles")

CONFIG_MAP = {
# "alacritty/": "~/.config/alacritty/",
    "rofi/": "/usr/share/fonts/wd",
}

dm.deploy_configs(CONFIG_MAP)
