# Даны имена четырёх файлов. Найти количество существующих среди них в текущем каталоге

import os

def count_existing_files(names: list[str]) -> int:
    count = 0
    for name in names:
        if os.path.isfile(name):
            count += 1
    return count
