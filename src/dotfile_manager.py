import os
import shutil
from pathlib import Path
from typing import Dict

class DotfileManager:
    def __init__(self, dotfiles_dir: str = "./dotfiles"):
        """
        :param dotfiles_dir: Путь к папке с исходными конфигами
        """
        self.dotfiles_dir = Path(dotfiles_dir).resolve()
        if not self.dotfiles_dir.exists():
            raise FileNotFoundError(f"Папка с конфигами не найдена: {self.dotfiles_dir}")


    def _backup_if_exists(self, target: Path):
        """Создаёт резервную копию существующего файла/папки."""
        if target.exists():
            backup = target.with_suffix(target.suffix + ".bak")
            if backup.exists():
                shutil.rmtree(backup) if backup.is_dir() else backup.unlink()
            if target.is_dir():
                shutil.copytree(target, backup)
            else:
                shutil.copy2(target, backup)
            print(f"⚠️  Существующий файл/папка сохранены как: {backup}")
            if target.is_dir():
                shutil.rmtree(target)
            else:
                target.unlink()


    def _copy_file_or_dir(self, source: Path, target: Path):
        """Копирует файл или директорию в целевое место."""
        self._backup_if_exists(target)

        target.parent.mkdir(parents=True, exist_ok=True)

        if source.is_dir():
            shutil.copytree(source, target)
            print(f"📁 Скопирована папка: {target}")
        else:
            shutil.copy2(source, target)
            print(f"📄 Скопирован файл: {target}")


    def deploy_configs(self, config_map: Dict[str, str]):
        """
        Копирует конфиги из dotfiles_dir в целевые пути.
        :param config_map: {"путь_в_dotfiles": "~/.config/..."}
        """
        for rel_source, rel_target in config_map.items():
            source = self.dotfiles_dir / rel_source
            if not source.exists():
                print(f"❌ Пропущен: {source} (не существует)")
                continue

            target = Path(os.path.expandvars(os.path.expanduser(rel_target)))

            self._copy_file_or_dir(source, target)