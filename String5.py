# Дано N (1 ≤ N ≤ 26). Вывести строку из N последних строчных латинских букв в обратном
# порядке, начиная с «z»

n = int(input())
result = ''.join(chr(ord('z') - i) for i in range(n))
print(result)
