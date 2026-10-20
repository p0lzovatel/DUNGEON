# Функция roots_count(a, b, c) возвращает число корней квадратного уравнения по
# дискриминанту D = b² − 4·a·c (a ≠ 0). Найти количество корней трёх уравнений

def roots_count(a, b, c):
    D = b**2 - 4*a*c
    if D > 0:
        return 2
    elif D == 0:
        return 1
    else:
        return 0

equations = [
    (1, -5, 6),   
    (1, 2, 1),    
    (1, 0, 1),    
]

for a, b, c in equations:
    print(f"Уравнение {a}x² + {b}x + {c}: корней = {roots_count(a, b, c)}")
