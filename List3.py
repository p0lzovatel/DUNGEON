# Дан список A из N чисел.
# Вывести сумму элементов и произведение элементов с чётными индексами (0, 2, 4…)

A = [2, 3, 4, 5, 6]

sum_even_idx = 0
prod_even_idx = 1

for i in range(0, len(A), 2):
    sum_even_idx += A[i]
    prod_even_idx *= A[i]

print(f"Сумма элементов с чётными индексами = {sum_even_idx}")
print(f"Произведение элементов с чётными индексами = {prod_even_idx}")
