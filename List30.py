# Дан список из N строк. Генератором вывести список длин строк и суммарную длину всех строк

strings = ["cat", "dog", "elephant", "fox"]

lengths_gen = (len(s) for s in strings)
lengths = list(lengths_gen)
total_length = sum(lengths)

print(lengths)
print(total_length)
