# Функция is_power5(k) возвращает True, если k (> 0) — степень пятёрки. Найти количество таких
# в наборе из 10 чисел

def is_power5(k):
    if k <= 0:
        return False
    while k % 5 == 0:
        k //= 5
    return k == 1

numbers = [1, 5, 10, 25, 50, 125, 200, 625, 1000, 3125]

count_powers5 = sum(1 for k in numbers if is_power5(k))
print("Количество степеней 5:", count_powers5)
