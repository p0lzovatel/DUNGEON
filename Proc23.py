# Функция quarter(x, y) возвращает номер координатной четверти точки с ненулевыми
# координатами. Найти четверти трёх точек

def quarter(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:  
        return 4

points = [
    (3, 5),
    (-2, 7),
    (-4, -1),
    (6, -8),
]

for x, y in points:
    print(f"Точка ({x}, {y}): четверть = {quarter(x, y)}")
