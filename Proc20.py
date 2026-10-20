# Функция triangle_p(a, h) возвращает периметр равнобедренного треугольника по основанию a
# и высоте h к основанию; боковая сторона b² = (a/2)² + h². Найти периметры трёх треугольников

import math

def triangle_p(a, h):
    half_base = a / 2
    side = math.sqrt(half_base**2 + h**2)
    return a + 2 * side

triangles = [
    (6, 4),
    (8, 3),
    (10, 12),
]

for a, h in triangles:
    print(f"Основание {a}, высота {h}: периметр = {triangle_p(a, h):.3f}")
