# Построить словарь из N пар. Удалить ключ K через pop с default:
# если ключа не было, словарь не меняется. Вывести размер после удаления

n = int(input())
d = {}
for _ in range(n):
    key, value = input().split()
    d[key] = int(value)

k = input()
d.pop(k, None)  
print(len(d))
