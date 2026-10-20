# Дан список A из N чисел и число D.
# Вывести число вхождений D (count) и индекс первого вхождения (или -1, если D нет)

A = [3, 7, 3, 9, 3]
D = 3

count_d = A.count(D)

if count_d == 0:
    first_index = -1
else:
    first_index = A.index(D)

print(f"Число вхождений {D} = {count_d}")
print(f"Индекс первого вхождения = {first_index}")
