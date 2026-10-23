# Построить словарь из N пар. Дан ключ K:
# вывести значение через get с default 0 одной строкой

n = int(input())
d = {}
for _ in range(n):
    key, value = input().split()
    d[key] = int(value)

k = input()
print(d.get(k, 0))
