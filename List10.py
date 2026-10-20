# Дан список из N строк.
# Вывести самую длинную и самую короткую строку (первую из встретившихся) и их длины

strings = ["cat", "elephant", "dog", "ant", "hippopotamus"]

longest = strings[0]
shortest = strings[0]

for s in strings:
    if len(s) > len(longest):
        longest = s
    if len(s) < len(shortest):
        shortest = s

print(f"Самая длинная строка: '{longest}', длина = {len(longest)}")
print(f"Самая короткая строка: '{shortest}', длина = {len(shortest)}")
