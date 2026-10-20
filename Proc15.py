# Функция shift_left3(a, b, c) возвращает тройку после левого циклического сдвига:
# a на место c, c на место b, b на место a. Сдвинуть два набора

def shift_left3(a, b, c):
    return b, c, a

sets = [
    (1, 2, 3),
    (7, 0, -5),
]

for s in sets:
    print(s, "->", shift_left3(*s))
