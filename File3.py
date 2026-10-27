# Дано имя файла и вещественные A и D. Записать в файл 10 первых членов прогрессии A, A+D,
# A+2·D, ...

def write_progression(filename: str, A: float, D: float) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        for i in range(10):
            value = A + i * D
            f.write(f"{value}\n")
