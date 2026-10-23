# Построить словарь из N пар. Вывести ключ с наибольшим значением (перебор с кандидатом;
# значения различны)

n = int(input())
d = {}
for _ in range(n):
    key, value = input().split()
    d[key] = int(value)

best_key = None
best_value = None

for key, value in d.items():
    if best_value is None or value > best_value:
        best_value = value
        best_key = key

print(best_key)
