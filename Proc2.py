# Функция power_a234(a) возвращает вторую, третью и четвёртую степени числа a.
# Найти три степени пяти данных чисел

def power_a234(a):
    return a**2, a**3, a**4

numbers = [2, 3, 5, 7, 10]

for n in numbers:
    p2, p3, p4 = power_a234(n)
    print(f"{n}: {p2}, {p3}, {p4}")
