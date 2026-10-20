# Дан список из N строк.
# Вывести строки в порядке возрастания длины и отдельно самую длинную (max с key)

strings = ["apple", "banana", "kiwi", "strawberry", "fig"]

sorted_by_len = sorted(strings, key=len)
longest = max(strings, key=len)

print(sorted_by_len)
print(longest)
