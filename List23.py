# Дан список A из N чисел. Вывести элементы в порядке убывания модуля
# (key=abs, reverse=True)

A = [3, -10, 2, -7, 1]

result = sorted(A, key=abs, reverse=True)
print(result)
