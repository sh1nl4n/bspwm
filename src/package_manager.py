import subprocess
import sys
from typing import List


class PackageManager:
	def __init__(self, aur_helper: str = "paru"):
		"""
		:param aur_helper: AUR-хелпер - "paru", "yay" и т.д.
		"""

		self.aur_helper = aur_helper
		self._validate_helpers()


	def _validate_helpers(self):
		"""Проверяет, установлены ли pacman и AUR-хелпер."""

		try:
				subprocess.run(["pacman", "--version"], stdout=subprocess.DEVNULL, check=True)
		except FileNotFoundError:
				sys.exit("❌ pacman не найден. Убедитесь, что вы в Arch Linux.")

		try:
				subprocess.run([self.aur_helper, "--version"], stdout=subprocess.DEVNULL, check=True)
		except FileNotFoundError:
				sys.exit(f"❌ AUR-хелпер '{self.aur_helper}' не найден. Установите его.")


	def is_installed(self, package: str) -> bool:
		"""Проверяет, установлен ли пакет"""

		try:
			result = subprocess.run(
				["pacman", "-Q", package],
				stdout=subprocess.DEVNULL,
				stderr=subprocess.DEVNULL,
				check=False
			)
			return result.returncode == 0
		except Exception:
			return False
		
	
	def install_package(self, packages: List[str], skip_installed: bool = True) -> None:
		"""
		Устанавливает список пакетов.
		:param packages: Список имен пакетов.
		:param skip_installed: Пропустить ли уже установленные пакеты.
		"""

		if not packages:
			print("ℹ️ Нет пакетов для установки.")
			return


		if skip_installed:
			packages = [p for p in packages if not self.is_installed(p)]

			if not packages:
				print("✅ Все пакеты уже установлены.")
				return

		print(f"📦 Установка {len(packages)} пакетов...")
		try:
			subprocess.run([self.aur_helper, "-S", "--needed", "--noconfirm"] + packages, check=True)
			print("✅ Установка завершена.")
		except subprocess.CalledProcessError as e:
			print(f"❌ Ошибка при установке: {e}")
			sys.exit(1)
		