# Дано число A (> 1). Вывести наибольшее из целых чисел K,
# для которых сумма 1 + 1/2 + ... + 1/K будет меньше A, и саму эту сумму.

A = float(input("Введите число A (> 1): "))

if A <= 1:
    print("Ошибка: число должно быть больше 1.")
else:
    k = 0
    total = 0.0
    while True:
        next_k = k + 1
        next_sum = total + 1 / next_k
        if next_sum >= A:
            break
        k = next_k
        total = next_sum
    print(f"Наибольшее целое K, при котором сумма 1 + 1/2 + ... + 1/K < {A}: {k}")
    print(f"Сама эта сумма: {total}")
