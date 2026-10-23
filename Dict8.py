# Построить словарь из N пар и число V. Вывести True, если V встречается среди значений,
# и False иначе

n = int(input())
d = {}
for _ in range(n):
    key, value = input().split()
    d[key] = int(value)

v = int(input())
print(v in d.values())
