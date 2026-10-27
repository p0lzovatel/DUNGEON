# Дана строка S. Если S — допустимое имя файла, создать пустой файл с этим именем и вывести
# True, иначе False

import os
import re

def is_valid_filename(name: str) -> bool:
    if not name:
        return False

    invalid_chars = r'[<>:"/\\|?*]'
    if re.search(invalid_chars, name):
        return False

    reserved = {
        "CON", "PRN", "AUX", "NUL",
        "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9",
        "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"
    }
    base = os.path.splitext(name)[0].upper()
    if base in reserved:
        return False

    return True

def create_if_valid(name: str) -> bool:
    if not is_valid_filename(name):
        return False
    try:

        with open(name, "wb") as f:
            pass
        return True
    except OSError:
        return False
