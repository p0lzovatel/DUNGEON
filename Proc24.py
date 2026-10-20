# Функция even(k) возвращает True для чётного k. Найти количество чётных в наборе из 10 чисел

def even(k):
    return k % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

count_even = sum(1 for k in numbers if even(k))
print("Количество чётных:", count_even)
