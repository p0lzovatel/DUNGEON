#  Функция digit_count(k) возвращает количество цифр k (> 0). Найти количество цифр пяти чисел

def digit_count(k):
    if k <= 0:
        return 0  
    count = 0
    while k > 0:
        count += 1
        k //= 10
    return count

numbers = [5, 42, 999, 1000, 78901]

for k in numbers:
    print(f"{k}: количество цифр = {digit_count(k)}")
