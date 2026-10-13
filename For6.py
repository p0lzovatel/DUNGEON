# Дано вещественное число — цена 1 кг конфет.
# Вывести стоимость 1.2, 1.4, ..., 2 кг конфет.

A = int(input('Введите цену за 1 кг'))

base = 1.2
step = 0.2
count = 5
for num in range(count):
    weight = base + num * step
    price = weight * A
    print(f'Цена за {weight} кг: {price}')