# Вывести элементы столбцов с нечётными номерами (1, 3, ...) по столбцам, без условного оператора

m = int(input())
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(m)]

for j in range(0, n, 2):          
    for i in range(m):           
        print(matrix[i][j])
