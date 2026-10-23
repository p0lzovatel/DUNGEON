# Построить словарь из N пар с различными значениями.
# Построить обращённый словарь: значение ключ. Вывести его пары в порядке добавления исходного

n = int(input())
d_forward = {}
order = [] 
for _ in range(n):
    key, value = input().split()
    value = int(value)
    d_forward[key] = value
    order.append(key)

d_reverse = {}
for key in order:
    val = d_forward[key]
    d_reverse[val] = key

for val, key in d_reverse.items():
    print(val, key)
