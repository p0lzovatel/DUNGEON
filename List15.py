# Дан список A из N чисел. Вывести элементы на нечётных позициях (1, 3, 5… при счёте позиций с 1) и их сумму

A = [10, 20, 30, 40, 50, 60]

odd_position_elements = A[::2]
sum_odd_positions = sum(odd_position_elements)

print("Элементы на нечётных позициях:", odd_position_elements)
print("Их сумма:", sum_odd_positions)
