# Дан список A из N чисел. Генератором вывести элементы, большие среднего, и само среднее

A = [4, 6, 2, 8, 10]

avg = sum(A) / len(A)
greater_than_avg_gen = (x for x in A if x > avg)

print(avg)
print(list(greater_than_avg_gen))
