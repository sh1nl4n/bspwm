ensure_dir() {
    local dir="$1"
    if [[ ! -d "$dir" ]]; then
        mkdir -p "$dir"
        echo "📁 Создана директория: $dir"
    else
        echo "✅ Директория уже существует: $dir"
    fi
}

copy_with_backup() {
    local src="$1"
    local dst="$2"

    if [[ ! -e "$src" ]]; then
        echo "❌ Ошибка: источник не существует: $src" >&2
        return 1
    fi

    # Создаём родительскую директорию для dst
    mkdir -p "$(dirname "$dst")"

    # Если dst существует — делаем бэкап
    if [[ -e "$dst" ]]; then
        local backup="${dst}.bak"
        rm -rf "$backup"
        if [[ -d "$dst" ]]; then
            cp -r "$dst" "$backup"
        else
            cp "$dst" "$backup"
        fi
        echo "⚠️  Сделан бэкап: $backup"
    fi

    # Копируем — с учётом содержимого каталога
    if [[ -d "$src" ]]; then
        # Удаляем dst, если он уже создан (чтобы избежать вложенности)
        rm -rf "$dst"
        # Копируем содержимое src в dst
        mkdir -p "$dst"
        cp -r "$src"/. "$dst"/
        echo "📁 Скопирована папка (содержимое): $src/ → $dst/"
    else
        cp "$src" "$dst"
        echo "📄 Скопирован файл: $src → $dst"
    fi
}

copy_with_backup ./dotfiles/bspwm ~/.config/bspwm

copy_with_backup ./dotfiles/sxhkd ~/.config/sxhkd

copy_with_backup ./dotfiles/dunst ~/.config/dunst

copy_with_backup ./dotfiles/picom ~/.config/picom

copy_with_backup ./dotfiles/gtk-3.0/settings.ini ~/.config/gtk-3.0/settings.ini

copy_with_backup ./dotfiles/gtk-4.0/settings.ini ~/.config/gtk-4.0/settings.ini

copy_with_backup ./dotfiles/betterlockscreen ~/.config/betterlockscreen

ensure_dir ~/Pictures/
cp -r ./dotfiles/pictures/* ~/Pictures/

copy_with_backup ./dotfiles/x11/xinitrc ~/.xinitrc

copy_with_backup ./dotfiles/x11/xsettingsd ~/.xsettingsd

copy_with_backup ./dotfiles/rofi/ ~/.config/rofi

copy_with_backup ./dotfiles/polybar/ ~/.config/polybar


copy_with_backup ./dotfiles/micro/ ~/.config/micro

copy_with_backup ./dotfiles/alacritty/ ~/.config/alacritty

ensure_dir ~/.local/share/fonts/
cp -r ./dotfiles/fonts/* ~/.local/share/fonts/

ensure_dir ~/.local/share/themes/
cp -r ./dotfiles/themes/* ~/.local/share/themes/

ensure_dir ~/.local/share/icons/
cp -r ./dotfiles/icons/* ~/.local/share/icons/

copy_with_backup ./dotfiles/bin ~/bin

sudo cp ./dotfiles/etc/logind.conf /etc/systemd/logind.conf

sudo cp ./dotfiles/x11/00-keyboard.conf /etc/X11/xorg.conf.d/00-keyboard.conf

sudo cp ./dotfiles/x11/50-touchpad.conf /etc/X11/xorg.conf.d/50-touchpad.conf


chmod +x ~/.config/bspwm/bspwmrc
chmod +x ~/.config/sxhkd/sxhkdrc
chmod +x ~/.config/polybar/launch.sh
chmod +x ~/.config/betterlockscreen/betterlockscreenrc
chmod +x ~/.xinitrc
chmod +x ~/.xsettingsd
chmod +x ~/bin/*

