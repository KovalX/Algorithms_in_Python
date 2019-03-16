# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.

a = [[6, 4, 8, 1, 15],
     [9, 2, 4, 3, 5],
     [15, 4, 7, 2, 17],
     [9, 12, 1, 0, 9]]

j = 0
max_num = 0

while j <= len(a):
    min_num = a[0][j]
    for i in range(len(a)):
        if a[i][j] <= min_num:
            min_num = a[i][j]
    if min_num > max_num:
        max_num = min_num
    #print(min_num, end=" ")
    j += 1


print("Максимальный элемент среди минимальных элементов столбцов матрицы:", max_num)
