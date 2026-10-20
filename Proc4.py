# Функция triangle_ps(a) возвращает периметр P = 3·a и площадь S = a²·√3/4
# равностороннего треугольника. Найти P и S трёх данных сторон

import math

def triangle_ps(a):
    P = 3 * a
    S = (a**2 * math.sqrt(3)) / 4
    return P, S

sides = [2, 5, 8]

for a in sides:
    P, S = triangle_ps(a)
    print(f"Сторона {a}: P = {P:.3f}, S = {S:.3f}")
