# Дано вещественное число — цена 1 кг конфет.
# Вывести стоимость 0.1, 0.2, ..., 1 кг конфет.

A = int(input('Введите цену за 1 кг'))

for num in range(1, 11):
    weight = num / 10
    price = weight * A
    print(f'Цена за {weight} кг конфет: {price}')