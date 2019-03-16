# 3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

a = list(map(int, input().split()))
print(a)

max_num = a[0]
min_num = a[0]

for i in range(len(a)):
    if a[i] > max_num:
        max_num = a[i]
    if a[i] < min_num:
        min_num = a[i]

for i in range(len(a)):
    if a[i] == max_num:
        a[i] = min_num
    elif a[i] == min_num:
        a[i] = max_num

print(a)
