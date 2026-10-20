# Функция sort_dec3(a, b, c) возвращает три значения по убыванию. Упорядочить два набора

def sort_dec3(a, b, c):
    if a < b:
        a, b = b, a
    if b < c:
        b, c = c, b
    if a < b:  
        a, b = b, a
    return a, b, c

sets = [
    (3, 1, 2),
    (10, 10, 5),
]

for s in sets:
    res = sort_dec3(*s)
    print(s, "->", res)
