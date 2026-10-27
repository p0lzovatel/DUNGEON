# Даны имена двух файлов: один существует и непуст (не обязательно первый), другой
# отсутствует. Создать отсутствующий и записать в него конечный и начальный элементы
# существующего

def copy_last_first(src: str, dst: str) -> None:
    with open(src, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    if not lines:
        raise ValueError("Существующий файл пуст")

    last = lines[-1]
    first = lines[0]

    with open(dst, "w", encoding="utf-8") as f:
        f.write(last + "\n")
        f.write(first + "\n")
