# Сформировать матрицу M × N, у которой все элементы J-го столбца равны 5·J (J = 1, ..., N)

m = int(input())
n = int(input())

matrix = []
for j in range(1, n + 1):
    col_val = 5 * j
    column = [col_val] * m
    matrix.append(column)

result = [[matrix[j][i] for j in range(n)] for i in range(m)]

for row in result:
    print(*row)
