# Функция minmax(x, y) возвращает пару (меньшее, большее).
# Четырьмя вызовами найти минимум и максимум четырёх данных чисел A, B, C, D

def minmax(x, y):
    if x <= y:
        return x, y
    else:
        return y, x

A, B, C, D = 7, 2, 9, 4

min1, max1 = minmax(A, B)
min2, max2 = minmax(C, D)

overall_min, _ = minmax(min1, min2)
_, overall_max = minmax(max1, max2)

print("Минимум:", overall_min)
print("Максимум:", overall_max)
