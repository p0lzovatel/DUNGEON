# Построить словарь из N пар. Дан ключ K:
# вывести его значение, если K есть, иначе строку «нет такого ключа» (через in)

n = int(input())
d = {}
for _ in range(n):
    key, value = input().split()
    d[key] = int(value)  

k = input()
if k in d:
    print(d[k])
else:
    print("нет такого ключа")
