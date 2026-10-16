# Та же задача, что Err5, но с двумя ветками: нечисловой индекс — «Ошибка ввода»,
# индекс вне границ — «Нет такого символа».

s = input()
index_str = input()
try:
    index = int(index_str)
except ValueError:
    print("Ошибка ввода")
else:
    if 0 <= index < len(s):
        print(s[index])
    else:
        print("Нет такого символа")
