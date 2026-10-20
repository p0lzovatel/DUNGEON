# Функция add_left_digit(d, k) возвращает число k с приписанной слева цифрой d (1–9).
# Приписать к данному K слева D1 и D2, печатая каждый шаг

def add_left_digit(d, k):
    if k == 0:
        return d
    temp = k
    multiplier = 1
    while temp > 0:
        multiplier *= 10
        temp //= 10
    return d * multiplier + k

K = 234
D1, D2 = 1, 9

step1 = add_left_digit(D1, K)
step2 = add_left_digit(D2, step1)

print(K, "->", step1, "->", step2)


