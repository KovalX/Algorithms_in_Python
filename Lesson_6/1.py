"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""

# Разрядность ОС: х64
# Версия Python: 3.6


import sys
from memory_profiler import profile


# Урок 2. Задача 7
# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

@profile
def func():
    a = list(range(500000))

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
    del a


'''
Для запуска программы было выделено 13.5 MiB.
При создании списка "a" было выделено еще 9.6 MiB.
После выполнения программы удалил список "a" , тем самым 
освободил память (9.6 MiB).


Line #    Mem usage    Increment   Line Contents
================================================
    16     13.5 MiB     13.5 MiB   @profile
    17                             def func():
    18     23.1 MiB      9.6 MiB       a = list(range(500000))
    19                             
    20     23.1 MiB      0.0 MiB       min_num = a[0]
    21     23.1 MiB      0.0 MiB       min_num2 = a[1]
    22                             
    23     23.1 MiB      0.0 MiB       if min_num > min_num2:
    24                                     min_num, min_num2 = min_num2, min_num
    25                             
    26     23.2 MiB      0.0 MiB       for i in range(len(a)):
    27     23.2 MiB      0.0 MiB           if a[i] < min_num:
    28                                         min_num2 = min_num
    29                                         min_num = a[i]
    30     23.2 MiB      0.0 MiB           elif a[i] < min_num2:
    31     23.1 MiB      0.0 MiB               min_num2 = a[i]
    32                             
    33     23.2 MiB      0.0 MiB       print("Два наименьших элемента:", min_num, min_num2)
    34     13.8 MiB      0.0 MiB       del a

'''


# Урок 3. Задача 2.	Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
# надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.


@profile
def func2():
    a = list(range(100000))
    b = []

    for i in range(len(a)):
        if a[i] % 2 == 0:
            b.append(i+1)

    del a
    return b

"""
Line #    Mem usage    Increment   Line Contents
================================================
    85     13.6 MiB     13.6 MiB   @profile
    86                             def func2():
    87     15.5 MiB      1.9 MiB       a = list(range(100000))
    88     15.5 MiB      0.0 MiB       b = []
    89                             
    90     16.9 MiB      0.1 MiB       for i in range(len(a)):
    91     16.9 MiB      0.0 MiB           if a[i] % 2 == 0:
    92     16.9 MiB      0.2 MiB               b.append(i+1)
    93                             
    94     14.8 MiB      0.0 MiB       del a
    95     14.8 MiB      0.0 MiB       return b

"""

# Урок 3. Задача 4. Определить, какое число в массиве встречается чаще всего.


@profile
def func3():
    a = [8, 6, 21, 17, 4, 8, 3, 13, 17, 4, 5, 96, 3, 11, 4, 8, 3, 9, 65]

    num = None
    n = 0

    for i in range(len(a)):
        if a.count(a[i]) > n:
            n = a.count(a[i])
            num = a[i]

    print(num)


"""
Line #    Mem usage    Increment   Line Contents
================================================
   114     13.7 MiB     13.7 MiB   @profile
   115                             def func3():
   116     13.7 MiB      0.0 MiB       a = [8, 6, 21, 17, 4, 8, 3, 13, 17, 4, 5, 96, 3, 11, 4, 8, 3, 9, 65]
   117                             
   118     13.7 MiB      0.0 MiB       num = None
   119     13.7 MiB      0.0 MiB       n = 0
   120                             
   121     13.7 MiB      0.0 MiB       for i in range(len(a)):
   122     13.7 MiB      0.0 MiB           if a.count(a[i]) > n:
   123     13.7 MiB      0.0 MiB               n = a.count(a[i])
   124     13.7 MiB      0.0 MiB               num = a[i]
   125                             
   126     13.7 MiB      0.0 MiB       print(num)
   
   
"""


if __name__ == "__main__":
    # func()
    # func2()
    func3()


