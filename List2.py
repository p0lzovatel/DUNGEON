# Дан список A из N чисел и индекс K (с 0).
# Вывести A[K], последний элемент и число элементов перед элементом с индексом K

A = [10, 20, 30, 40, 50]
K = 2

element_k = A[K]
last_element = A[-1]
elements_before_k = K 

print(f"A[K] = {element_k}")
print(f"Последний элемент = {last_element}")
print(f"Число элементов перед A[{K}] = {elements_before_k}")
