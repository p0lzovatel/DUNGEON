# Функция add_right_digit(d, k) возвращает число k с приписанной справа цифрой d (0–9).
# Приписать к данному K справа D1 и D2, печатая результат каждого шага

def add_right_digit(d, k):
    return k * 10 + d

K = 123
D1, D2 = 4, 5

step1 = add_right_digit(D1, K)
step2 = add_right_digit(D2, step1)

print(K, "->", step1, "->", step2)
