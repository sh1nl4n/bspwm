class Packages:
	# === BASE ===
	base = [
		"bspwm", 								# Tiling-манеджер окон (база окружения)
		"sxhkd", 								# Hotkey daemon для bspwm (обработка клавиш)
		"xorg-server", 					# X11-сервер (графическая подсистема)
		"xorg-xinit", 					# Утилита startx для запуска X-сессий
		"xorg-xrandr",					# Управление мониторами и разрешением
		"xorg-xinput",					# Настройка устройств ввода (мышь, тачпад)	
		"xorg-xdpyinfo",				# Диагностика X11 (информация о дисплеях)
		"xorg-xkill",						# Принудительное закрытие зависших окон
		"libinput-gestures",		# Жесты 
		"xf86-input-libinput",  # Современный драйвер ввода для клавиатуры, тачпадов
		"alacritty"
	]


	# === Панель, композинг, обои, уведомления ===
	desktop = [
		"polybar",              # Современная панель 
		"picom",								# Композитный менеджер (прозрачность, тени, плавность)
		"dunst",								# Легкий демон уведомлений
		"feh",									# Установка обоев и просмотр изображений 
		"rofi",									# Меню запуска
		"rofi-calc",						# Калькулятор внутри rofi
		"cliphist",							# История буфера обмена
		"xclip",								# Классический инструмент для работы с буфером в X11
		"lxappearance",
		"autorandr"
	]


	# === УПРАВЛЕНИЕ СЕССИЯМИ ===
	session = [
		"xss-lock",             # Блокирует экран при простое или перед сном (интеграция с logind)
		"betterlockscreen",     # Красивая блокировка экрана с размытием и изображениями
		"ly",                   # Консольный дисплей-менеджер (альтернатива GDM/SDDM)
	]


	# ==== СЕТЬ ===
	network = [
		"networkmanager",       # Управление сетевыми подключениями (Wi-Fi, Ethernet)
		"network-manager-applet",  # Иконка сети в трее (для совместимости с GTK-панелями)
		"nm-connection-editor", # Графический редактор подключений NetworkManager
		"networkmanager-openvpn",  # Поддержка OpenVPN в NetworkManager
		"iwd",                  # Современная замена wpa_supplicant для Wi-Fi
		"wpa_supplicant",       # Стандартный демон для подключения к защищённым Wi-Fi
		"dnsmasq",              # Локальный DNS/DHCP-сервер (для маршрутизации или тестов)
		"rsync",                # Синхронизация файлов по сети
		"wget",                 # Загрузка файлов из командной строки
		"openssh",              # SSH-клиент и сервер для удалённого доступа
	]


	# === ЗВУК ===
	sound = [
		"pipewire",             # Современная аудио/видео система (заменяет PulseAudio + JACK)
		"pipewire-pulse",       # Совместимость с PulseAudio-приложениями
		"pipewire-alsa",        # Поддержка ALSA-приложений в PipeWire
		"wireplumber",          # Менеджер сессий для PipeWire (рекомендуется)
		"pavucontrol",          # Графический микшер громкости для PulseAudio/PipeWire
		"pamixer",              # Управление громкостью из терминала
		"alsa-utils",           # Утилиты alsamixer, amixer и др. для низкоуровневого контроля
		"alsa-plugins",         # Дополнительные плагины ALSA (включая PulseAudio-мост)
		"gst-plugins-bad",      # Дополнительные медиа-кодеки через GStreamer
		"gst-plugins-ugly",     # Патентованные/проприетарные кодеки GStreamer
		"gst-libav",            # Поддержка FFmpeg-кодеков в GStreamer
		"ffmpegthumbnailer",    # Генерация превью видео (для файловых менеджеров)
	]


	# === BLUETOOTH ===
	bluetooth = [
		"bluez",                # Основной стек Bluetooth
		"bluez-utils",          # Утилиты командной строки: bluetoothctl и др.
		"bluez-hid2hci",        # Переключение Bluetooth-устройств из HID в HCI-режим
		"bluez-libs",           # Библиотеки для разработки/интеграции с BlueZ
	]


	# === ШРИФТЫ ===
	fonts = [
		"awesome-terminal-fonts",  # Иконки для терминала и панелей (часто используется в polybar)
		"ttf-hack",             # Моноширинный шрифт для кода
		"ttf-iosevka-nerd",     # Nerd Fonts версия Iosevka (с иконками)
		"ttf-meslo-nerd",       # Популярный Nerd Font для терминалов
		"ttf-nerd-fonts-symbols-common",  # Общие символы Nerd Fonts
		"ttf-nerd-fonts-symbols-mono",    # Моноширинные иконки Nerd Fonts
		"ttf-zed-mono-nerd",    # Nerd Font от редактора Zed
		"noto-fonts",           # Универсальные шрифты Google (латиница, кириллица и др.)
		"noto-fonts-cjk",       # Noto для китайского, японского, корейского
		"noto-fonts-emoji",     # Цветные эмодзи от Google
		"adobe-source-han-sans-cn-fonts",  # Adobe Sans для упрощённого китайского
		"adobe-source-han-sans-jp-fonts",  # Adobe Sans для японского
		"adobe-source-han-sans-kr-fonts",  # Adobe Sans для корейского
		"opendesktop-fonts",    # Дополнительные CJK-шрифты
		"ttf-bitstream-vera",   # Классический свободный шрифт
		"ttf-dejavu",           # Расширенный шрифт с поддержкой множества символов
		"ttf-liberation",       # Замена Arial/Times New Roman
		"ttf-opensans",         # Современный sans-serif шрифт
		"otf-font-awesome",     # Иконки Font Awesome (для веб и UI)
		"woff2-font-awesome",   # WOFF2-версия Font Awesome (для браузеров)
	]



	# === СИСТЕМНЫЙ МОНИТОРИНГ И УТИЛИТЫ ===
	system = [
		"htop",                 # Интерактивный монитор процессов
		"btop",                 # Улучшенная альтернатива htop с графикой
		"nvtop",                # Мониторинг GPU (NVIDIA/AMD/Intel)
		"glances",              # Многофункциональный системный монитор
		"duf",                  # Современная замена df (информация о дисках)
		"fastfetch",            # Быстрый аналог neofetch с кастомизацией
		"neofetch",             # Отображение информации о системе и логотипа
		"smartmontools",        # Мониторинг состояния дисков (SMART)
		"hdparm",               # Настройка и тестирование HDD/SSD
		"ethtool",              # Диагностика и настройка сетевых интерфейсов
		"dmidecode",            # Информация о железе (BIOS, материнка, RAM)
		"lsb-release",          # Информация о дистрибутиве
		"sysfsutils",           # Утилиты для работы с sysfs
		"less",                 # Постраничный просмотр текста
		"man-db",               # Система man-страниц
		"man-pages",            # Сами man-страницы
		"logrotate",            # Ротация лог-файлов
		"haveged",              # Генератор энтропии для ускорения криптографии
		"pkgfile",              # Поиск пакета по имени файла
		"plocate",              # Быстрый поиск файлов (современная замена locate)
		"ripgrep",              # Очень быстрый grep-аналог
	]


	# === ФАЙЛОВЫЕ СИСТЕМЫ И ДИСКИ ===
	storage = [
		"btrfs-progs",          # Утилиты для работы с Btrfs
		"btrfs-assistant",      # GUI-помощник для Btrfs (снапшоты и др.)
		"snapper",              # Управление снапшотами Btrfs
		"lvm2",                 # Logical Volume Manager
		"mdadm",                # Управление RAID-массивами
		"xfsprogs",             # Утилиты для XFS
		"jfsutils",             # Утилиты для JFS
		"nilfs-utils",          # Утилиты для NILFS2
		"exfatprogs",           # Поддержка exFAT (современная)
		"dosfstools",           # Поддержка FAT32
		"mtools",               # Работа с FAT без монтирования
		"fsarchiver",           # Архивирование разделов
		"gparted",   # GUI для управления дисками (Disks)
	]

	
	# === ПРИЛОЖЕНИЯ: браузеры, мессенджеры, IDE, контейнеры ===
	apps = [
		"chromium",             # Альтернативный браузер
		"zen-browser-bin",      # Минималистичный Firefox-форк
		"yandex-browser",       # Браузер от Яндекса
		"nekoray-bin",          # GUI для Xray/V2Ray
		"obs-studio",           # Запись экрана и стриминг
		"visual-studio-code-bin",  # Популярный редактор кода
		"zed",                  # Современный многопользовательский редактор
		"micro",                # Простой терминальный текстовый редактор
		"neovim",               # Современный Vim
		"vim",                  # Классический Vim
		"nano",                 # Простой редактор для новичков
		"tmux",                 # Мультиплексор терминала
		"ranger",               # Терминальный файловый менеджер
		"yazi",                 # Быстрый файловый менеджер на Rust
		"zoxide",               # Умная навигация по директориям (альтернатива cd)
		"starship",             # Кастомизируемый приглашение командной строки
		"git",                  # Система контроля версий
		"docker",               # Контейнеризация
		"docker-compose",       # Управление многоконтейнерными приложениями
		"meld",                 # Визуальное сравнение файлов
		"octopi",               # GUI для pacman (менеджер пакетов)
		# "paru-bin",                 # AUR-хелпер (альтернатива yay)
		# "yay-bin",              # Ещё один популярный AUR-хелпер
		"nodejs",
		"npm",
		"gpick"
	]


	# === GAMES ===
	games = [
		"steam-native-runtime", # Steam без собственного рантайма
		"lutris",
		"wine-staging",         # Запуск Windows-приложений
		"winetricks",           # Установка зависимостей для Wine
		"protonup-qt-bin",      # Управление Proton-версиями для Steam
		"wine-mono", 
		"giflib", 
		"lib32-giflib", 
		"libpng", 
		"lib32-libpng", 
		"libldap", 
		"lib32-libldap", 	
		"gnutls", 	
		"lib32-gnutls", 	
		"mpg123", 	
		"lib32-mpg123", 	
		"openal", 	
		"lib32-openal", 	
		"v4l-utils", 	
		"lib32-v4l-utils", 	
		"libpulse", 	
		"lib32-libpulse", 	
		"libgpg-error", 	
		"lib32-libgpg-error", 	
		"alsa-plugins", 	
		"lib32-alsa-plugins", 	
		"alsa-lib", 	
		"lib32-alsa-lib", 	
		"libjpeg-turbo", 	
		"lib32-libjpeg-turbo", 	
		"sqlite", 	
		"lib32-sqlite", 	
		"libxcomposite", 	
		"lib32-libxcomposite", 	
		"libxinerama", 	
		"lib32-libgcrypt", 	
		"libgcrypt", 	
		"lib32-libxinerama", 	
		"ncurses", 	
		"lib32-ncurses", 	
		"opencl-icd-loader", 	
		"lib32-opencl-icd-loader", 	
		"libxslt", 	
		"lib32-libxslt", 	
		"libva", 	
		"lib32-libva", 	
		"gtk3", 	
		"lib32-gtk3", 	
		"gst-plugins-base-libs", 	
		"lib32-gst-plugins-base-libs", 	
		"vulkan-icd-loader", 	
		"lib32-vulkan-icd-loader"
	]


	gnome_essential_for_wm = [
    "gnome-keyring",           # хранение паролей Git, Wi-Fi и т.д.
    "xdg-desktop-portal-gnome",# порталы: скриншоты, файлы, камера (для Firefox, Chromium)
    "gvfs",                    # поддержка MTP, SMB, Google Drive в файловых менеджерах
    "upower",                  # информация о батарее (для polybar)
    "polkit-gnome",            # диалоги авторизации (например, при монтировании диска)
	]
