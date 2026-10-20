# Дан список из N строк и буква.
# Генератором вывести строки, начинающиеся с этой буквы (первый символ строки)

strings = ["apple", "apricot", "banana", "avocado", "cherry"]
letter = "a"

filtered_gen = (s for s in strings if s.startswith(letter))
print(list(filtered_gen))
