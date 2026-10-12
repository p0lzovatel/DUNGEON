# Даны три целых числа.
# Найти количество положительных и количество отрицательных чисел в исходном наборе.

A = int(input('Введите первое целое число'))
B = int(input('Введите второе число'))
C = int(input('Введите третье число'))

list = [A, B, C]
positive = []
negative = []
for number in list:
    if number > 0:
        positive.append(number)
    else:
        negative.append(number)
print(f'Количество положительных чисел:', len(positive), 'количество отрицательных:', len(negative))