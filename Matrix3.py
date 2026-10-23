# Даны M, N и набор из M чисел. Сформировать матрицу, у которой в каждом столбце
# содержатся все числа набора в том же порядке

m = int(input())
n = int(input())
col_data = [int(input()) for _ in range(m)]

matrix = [[col_data[i]] * n for i in range(m)]

for row in matrix:
    print(*row)
