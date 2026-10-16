# Прочитать целое число. При ошибке вывести текст исключения и его тип отдельными строками,
# пользуясь as e и type(e). При успехе вывести само число.

try:
    number = int(input())
    print(number)
except Exception as e:
    print(type(e).__name__)
    print(e)
