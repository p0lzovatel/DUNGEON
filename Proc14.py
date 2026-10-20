# Функция shift_right3(a, b, c) возвращает тройку после правого циклического сдвига:
# a переходит на место b, b — на место c, c — на место a. Сдвинуть два набора

def shift_right3(a, b, c):
    return c, a, b

sets = [
    (1, 2, 3),
    (7, 0, -5),
]

for s in sets:
    print(s, "->", shift_right3(*s))
