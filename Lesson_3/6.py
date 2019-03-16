"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

a = [87, 42, 2, 12, 5, 9, 32, 55, 97, 36, 4, 8]
print(sum(a[a.index(min(a))+1:a.index(max(a))]))

'''
a = [87, 42, 2, 12, 5, 9, 32, 55, 97, 36, 4, 8]

max_num = a[0]
min_num = a[0]

for i in range(len(a)):
    if a[i] > max_num:
        max_num = a[i]
    if a[i] < min_num:
        min_num = a[i]

max_index = a.index(max_num)
min_index = a.index(min_num)

print(sum(a[min_index+1:max_index]))
'''