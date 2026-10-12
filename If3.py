# Даны три целых числа. Найти количество положительных чисел в исходном наборе.

A = int(input('Введите первое целое число'))
B = int(input('Введите второе число'))
C = int(input('Введите третье число'))

list = [A, B, C]
positive = []
for number in list:
    if number > 0:
        positive.append(number)  
print(f'Количество положительных чисел:', len(positive))
        