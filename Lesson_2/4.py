"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

n = int(input("Введите количество элементов: "))
sum_num = 0
current_num = 1

for _ in range(n-1):
    current_num = current_num / -2
    sum_num += current_num

print("Сумма:", sum_num + 1)

