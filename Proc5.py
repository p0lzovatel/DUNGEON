# Функция rect_ps(x1, y1, x2, y2) возвращает периметр и площадь прямоугольника со сторонами,
# параллельными осям, по противоположным вершинам. Найти P и S трёх прямоугольников

def rect_ps(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    P = 2 * (dx + dy)
    S = dx * dy
    return P, S

rects = [
    (0, 0, 4, 3),
    (-1, -2, 2, 1),
    (5, 5, 10, 7),
]

for i, (x1, y1, x2, y2) in enumerate(rects, start=1):
    P, S = rect_ps(x1, y1, x2, y2)
    print(f"Прямоугольник {i}: P = {P}, S = {S}")
