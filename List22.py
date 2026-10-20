# Дан список A из N чисел и число D.
# Генератором вывести элементы, умноженные на D, и количество элементов, равных D

A = [2, 5, 5, 3, 5]
D = 5

multiplied_gen = (x * D for x in A)
count_equal_D = sum(1 for x in A if x == D)

print(list(multiplied_gen))
print(count_equal_D)
