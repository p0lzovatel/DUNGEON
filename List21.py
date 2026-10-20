# Дан список A из N чисел.
# Генератором с фильтром вывести только положительные элементы и их количество

A = [3, -1, 0, 7, -5, 2]

positive_gen = (x for x in A if x > 0)
positive_list = list(positive_gen)

print(positive_list)
print(len(positive_list))
