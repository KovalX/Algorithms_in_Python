"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

a = [87, 42, 2, 12, 5, 9, 32, 55, 97, 36, 4, 8, 4]

min_num = a[0]
min_num2 = a[1]

if min_num > min_num2:
    min_num, min_num2 = min_num2, min_num

for i in range(len(a)):
    if a[i] < min_num:
        min_num2 = min_num
        min_num = a[i]
    elif a[i] < min_num2:
        min_num2 = a[i]

print("Два наименьших элемента:", min_num, min_num2)
