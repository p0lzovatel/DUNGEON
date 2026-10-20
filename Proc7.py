# Функция invert_digits(k) возвращает число с обратным порядком цифр. Перевернуть пять данных чисел

def invert_digits(k):
    k = abs(k)  
    reversed_num = 0
    while k > 0:
        digit = k % 10
        reversed_num = reversed_num * 10 + digit
        k //= 10
    return reversed_num

numbers = [123, 9070, 500, 1000, 98765]

for n in numbers:
    print(n, "->", invert_digits(n))
