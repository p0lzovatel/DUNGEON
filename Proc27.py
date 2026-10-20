# Функция is_power_n(k, n) возвращает True, если k (> 0) — степень n (> 1). Даны n и набор из 10
# чисел: найти количество степеней

def is_power_n(k, n):
    if k <= 0 or n <= 1:
        return False
    while k % n == 0:
        k //= n
    return k == 1

n = 3
numbers = [1, 3, 6, 9, 27, 54, 81, 162, 243, 1000]

count_powers_n = sum(1 for k in numbers if is_power_n(k, n))
print(f"Количество степеней {n}: {count_powers_n}")
