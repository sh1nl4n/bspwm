#!/bin/bash

set -euo pipefail  # Строгий режим: остановка при ошибках

# === Настройки ===
AUR_HELPER="${AUR_HELPER:-yay}"  # можно переопределить: AUR_HELPER=yay ./install-packages.sh
PACKAGES_FILE="${PACKAGES_FILE:-packages.list}"  # файл со списком пакетов (по одному на строку)

# === Проверка зависимостей ===
if ! command -v "$AUR_HELPER" &> /dev/null; then
    echo "❌ AUR-хелпер '$AUR_HELPER' не найден. Установите его (paru, yay и т.д.)."
    exit 1
fi

# === Функция: установлен ли пакет? ===
is_installed() {
    local pkg="$1"
    if pacman -Q "$pkg" &> /dev/null; then
        return 0
    else
        return 1
    fi
}

# === Чтение списка пакетов ===
if [[ ! -f "$PACKAGES_FILE" ]]; then
    echo "⚠️  Файл '$PACKAGES_FILE' не найден. Используется встроенный список."
    # Можно задать встроенный список вместо файла:
    read -r -d '' PKG_LIST <<EOF || true
bspwm
sxhkd
polybar
picom
dunst
feh
lxappearance
xss-lock
gparted
gpick
lutris
libinput-gestures
EOF
    mapfile -t PACKAGES <<< "$PKG_LIST"
else
    # Читаем непустые строки, игнорируя комментарии (#)
    mapfile -t PACKAGES < <(grep -v '^[[:space:]]*#' "$PACKAGES_FILE" | grep -v '^[[:space:]]*$')
fi

# === Фильтрация: оставить только неустановленные ===
TO_INSTALL=()
for pkg in "${PACKAGES[@]}"; do
    pkg="${pkg%%#*}"      # удаляем комментарии в строке (на случай)
    pkg="${pkg// /}"      # удаляем пробелы
    if [[ -z "$pkg" ]]; then
        continue
    fi
    if is_installed "$pkg"; then
        echo "✅ Уже установлен: $pkg"
    else
        TO_INSTALL+=("$pkg")
        echo "📥 Будет установлен: $pkg"
    fi
done

# === Установка ===
if [[ ${#TO_INSTALL[@]} -eq 0 ]]; then
    echo -e "\n🎉 Все пакеты уже установлены!"
    exit 0
fi

echo -e "\n📦 Установка ${#TO_INSTALL[@]} пакетов через $AUR_HELPER..."
echo "⚠️  Может потребоваться ввести пароль sudo."

# Передаём пакеты напрямую — AUR-хелпер сам запросит sudo при необходимости
if ! "$AUR_HELPER" -S --needed --noconfirm "${TO_INSTALL[@]}"; then
    echo "❌ Ошибка при установке пакетов."
    exit 1
fi

echo -e "\n✅ Установка завершена!"