# Функция is_square(k) возвращает True, если k (> 0) — квадрат целого числа. Найти количество
# квадратов в наборе из 10 чисел

import math

def is_square(k):
    if k <= 0:
        return False
    root = int(math.isqrt(k)) 
    return root * root == k

numbers = [1, 2, 4, 8, 9, 15, 16, 24, 25, 30]

count_squares = sum(1 for k in numbers if is_square(k))
print("Количество квадратов:", count_squares)
