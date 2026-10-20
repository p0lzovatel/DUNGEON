# Дан список A из N различных чисел. Вывести второй по величине элемент 

A = [10, 3, 8, 15, 7] 

second_largest = sorted(set(A))[-2]
print(second_largest)
