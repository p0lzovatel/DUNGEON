# Дана строка. Подсчитать количество прописных латинских букв в ней

s = input()
count = sum(1 for ch in s if 'A' <= ch <= 'Z')
print(count)
