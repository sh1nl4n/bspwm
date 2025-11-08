#!/bin/sh

# Получаем ID окна
wid="$1"

# Получаем класс и instance
class=$(xprop -id "$wid" WM_CLASS 2>/dev/null | cut -d '"' -f 4 | head -n1)
instance=$(xprop -id "$wid" WM_CLASS 2>/dev/null | cut -d '"' -f 2)
name=$(xprop -id "$wid" WM_NAME 2>/dev/null | cut -d '"' -f 2)
types=$(xprop -id "$wid" _NET_WM_WINDOW_TYPE 2>/dev/null)

# Проверяем, похоже ли это на PiP из Firefox/Zen
if [ "$class" = "zen" ] && [ "$instance" = "Toolkit" ]; then
    # Дополнительная проверка: тип окна — UTILITY и короткое имя (или содержит "Picture")
    if echo "$types" | grep -q "_NET_WM_WINDOW_TYPE_UTILITY"; then
        if [ -n "$name" ] && [ "${#name}" -le 30 ]; then
            # Скорее всего — PiP
            echo "state=floating"
            echo "sticky=on"
            echo "rectangle=701x398+160+90"
            exit 0
        fi
    fi
fi

# По умолчанию — ничего не делать
exit 1
