# Дан список A из N чисел.
# Вывести элементы, большие среднего арифметического всех элементов, и их количество

A = [1, 5, 3, 9, 7]

avg = sum(A) / len(A)
greater_than_avg = [x for x in A if x > avg]

print(f"Среднее арифметическое = {avg}")
print("Элементы больше среднего:", greater_than_avg)
print("Количество таких элементов:", len(greater_than_avg))
