# Функция sum_range(a, b) возвращает сумму целых от a до b включительно; если a > b,
# возвращает 0. Найти суммы от A до B и от B до C

def sum_range(a, b):
    if a > b:
        return 0
    n = b - a + 1
    return n * (a + b) // 2

A, B, C = 3, 7, 2

sum1 = sum_range(A, B)
sum2 = sum_range(B, C)

print(f"Сумма от {A} до {B}: {sum1}")
print(f"Сумма от {B} до {C}: {sum2}")
