# Построить словарь из N троек: название, цена, количество (значение — список из двух чисел).
# Вывести суммарную стоимость склада и название самого дорогого по стоимости предмета

n = int(input())
d = {}
total_cost = 0
best_item = None
best_item_cost = -1

for _ in range(n):
    name, price, qty = input().split()
    price = int(price)
    qty = int(qty)
    cost = price * qty
    d[name] = [price, qty]
    total_cost += cost

    if cost > best_item_cost:
        best_item_cost = cost
        best_item = name

print(total_cost)
print(best_item)
