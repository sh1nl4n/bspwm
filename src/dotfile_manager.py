import os
import shutil
import subprocess
from pathlib import Path
from typing import Dict, List


class DotfileManager:
    def __init__(self, dotfiles_dir: str = "./dotfiles"):
        """
        :param dotfiles_dir: Путь к папке с исходными конфигами (относительно скрипта или абсолютный)
        """

        self.dotfiles_dir = Path(dotfiles_dir).resolve()
        if not self.dotfiles_dir.exists():
            raise  FileNotFoundError(f"Папка с конфигами не найдена: {self.dotfiles_dir}")


    def _ensure_dir(self, target_dir: Path):
        """Создает родительскую директорию, если ее нет"""

        target_dir.mkdir(parents=True, exist_ok=True)


    def symlink_file(self, source: Path, target: Path):
        """Создает симолическую ссылку (перезаписывает, если существует)"""

        if target.exists() or target.is_symlink():
            if target.is_symlink():
                target.unlink()
            else:
                backup = target.with_suffix(target.suffix + ".bak")
                shutil.move(str(target), str(backup))
                print(f"⚠️  Существующий файл сохранён как: {backup}")

        self._ensure_dir(target.parent)
        target.symlink_to(source)
        print(f"🔗 Создана ссылка: {target} → {source}")

    def deploy_configs(self, config_map: Dict[str, str]):
        """
        Разворачивает конфиги по заданной карте.
        :param config_map: { "путь_в_dotfiles": "$XDG_CONFIG_HOME/..." или "~/.имя" }
        """
        for rel_source, rel_target in config_map.items():
            source = self.dotfiles_dir / rel_source
            if not source.exists():
                print(f"❌ Пропущен: {source} (не существует)")
                continue

            target = os.path.expandvars(os.path.expanduser(rel_target))
            target_path = Path(target)

            if source.is_dir():
                if target_path.exists():
                    shutil.rmtree(target_path)
                shutil.copytree(source, target_path)
                print(f"📁 Скопирована папка: {target_path}")
            else:
                self.symlink_file(source, target_path)