# Построить словарь из N пар и число V. Удалить все пары со значением меньше V,
# не меняя словарь во время перебора. Вывести размер после удаления

n = int(input())
d = {}
for _ in range(n):
    key, value = input().split()
    d[key] = int(value)

v = int(input())

keys_to_remove = [k for k, val in d.items() if val < v]
for k in keys_to_remove:
    del d[k]

print(len(d))
