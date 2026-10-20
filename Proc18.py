# Proc18 Функция circle_s(r) возвращает площадь круга радиуса r (π = 3.14). Найти площади трёх кругов

PI = 3.14

def circle_s(r):
    return PI * r**2

radii = [1, 2.5, 10]

for r in radii:
    print(f"Радиус {r}: площадь = {circle_s(r):.2f}")
