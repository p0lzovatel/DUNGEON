# Даны M, N, число D и набор из M чисел. Первый столбец — набор; каждый следующий столбец
# равен предыдущему плюс D по строкам

m = int(input())
n = int(input())
d = int(input())
first_col = [int(input()) for _ in range(m)]

matrix = [first_col[:]] 

for _ in range(1, n):
    prev = matrix[-1]
    curr = [prev[i] + d for i in range(m)]
    matrix.append(curr)

for i in range(m):
    row = [matrix[j][i] for j in range(n)]
    print(*row)
