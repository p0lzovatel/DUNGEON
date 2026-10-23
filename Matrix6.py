# Даны M, N, число Q и набор из N чисел. Первая строка — набор; каждая следующая строка
# равна предыдущей, умноженной на Q по столбцам

m = int(input())
n = int(input())
q = int(input())
first_row = [int(input()) for _ in range(n)]

matrix = [first_row]

for _ in range(1, m):
    prev = matrix[-1]
    curr = [x * q for x in prev]
    matrix.append(curr)

for row in matrix:
    print(*row)
