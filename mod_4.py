"""
# Задание 4
# Имеется папка с файлами
# Реализовать удаление файлов старше N дней

"""

import os
import time
from pathlib import Path

name_dir = '.'  # Директория
old_day = 7  # Количество дней


# Вариант 1
for dirpath, dirnames, filenames in os.walk("."):
    # перебрать файлы
    for filename in filenames:
        print("Файл:", os.path.join(dirpath, filename))
        if os.stat(os.path.join(dirpath, filename)).st_mtime < (time.time() - old_day * 86400):
            if os.path.isfile(os.path.join(dirpath, filename)):
                print(f'Удаленный файл: {os.path.join(dirpath, filename)}')
                os.remove(os.path.join(dirpath, filename))


# Вариант 2
for item in Path(name_dir).glob('*'):
    if item.is_file():
        print(str(item.absolute()))
        if item.stat().st_mtime < (time.time() - old_day * 86400):
            print(f'Удаленный файл: {item}')
            os.remove(item.absolute())
