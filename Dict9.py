# Построить словари из N и M пар. Слить второй в первый через update. Вывести размер
# результата и значение ключа, который был в обоих словарях (такой ключ гарантированно есть)

n = int(input())
d1 = {}
for _ in range(n):
    key, value = input().split()
    d1[key] = int(value)

m = int(input())
d2 = {}
for _ in range(m):
    key, value = input().split()
    d2[key] = int(value)

common_key = None
for k in d1:
    if k in d2:
        common_key = k
        break

d1.update(d2)
print(len(d1))
print(d1[common_key])
