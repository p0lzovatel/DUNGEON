# Дана строка. Подсчитать общее количество строчных латинских и русских букв в ней

s = input()
lower_latin = sum(1 for ch in s if 'a' <= ch <= 'z')
lower_rus = sum(1 for ch in s if 'а' <= ch <= 'я' or ch == 'ё' or ch == 'Ё')
lower_rus_only = sum(1 for ch in s if ('а' <= ch <= 'я') or ch == 'ё')

print(lower_latin + lower_rus_only)
