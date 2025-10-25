ensure_dir() {
    local dir="$1"
    if [[ ! -d "$dir" ]]; then
        mkdir -p "$dir"
        echo "📁 Создана директория: $dir"
    else
        echo "✅ Директория уже существует: $dir"
    fi
}



sudo pacman -S stow

cd ~/dotfiles || exit 1

PACKAGES=(
    alacritty
    betterlockscreen
    bin
    bspwm
    dunst
    fonts
    icons
    micro
    picom
    polybar
    rofi
    sxhkd
    themes
    xinit
    yazi
    nekoray
    vim
)

echo "🔗 Устанавливаю dotfiles через stow..."

for pkg in "${PACKAGES[@]}"; do
    if [[ -d "$pkg" ]]; then
        echo "📦 $pkg"
        stow --dotfiles -v -t ~ "$pkg"
    else
        echo "⚠️  Пропущен: $pkg (папка не найдена)"
    fi
done

# Выставляем права на исполняемые файлы
chmod +x ~/.config/bspwm/bspwmrc
chmod +x ~/.config/sxhkd/sxhkdrc
chmod +x ~/.config/polybar/launch.sh
chmod +x ~/.config/betterlockscreen/betterlockscreenrc
chmod +x ~/.xinitrc
chmod +x ~/bin/*

echo "✅ Готово!"

sudo cp ./etc/logind.conf /etc/systemd/logind.conf
sudo cp ./x11/00-keyboard.conf /etc/X11/xorg.conf.d/
sudo cp ./x11/50-touchpad.conf /etc/X11/xorg.conf.d/


ensure_dir ~/Pictures/
cp -r ./pictures/* ~/Pictures/



