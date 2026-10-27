# Даны имена двух файлов: первый существует и непуст, второй отсутствует. Создать второй и
# записать в него первый и последний элементы первого

def copy_first_last(src: str, dst: str) -> None:
    with open(src, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    if not lines:
        raise ValueError("Исходный файл пуст")

    first = lines[0]
    last = lines[-1]

    with open(dst, "w", encoding="utf-8") as f:
        f.write(first + "\n")
        f.write(last + "\n")
