# Построить словари из N и M пар. Добавить в первый пары второго без update: только ключи,
# которых нет; совпавшие ключи считать проигнорированными. Вывести размер и число проигнорированных

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

ignored = 0
for k, v in d2.items():
    if k not in d1:
        d1[k] = v
    else:
        ignored += 1

print(len(d1), ignored)
