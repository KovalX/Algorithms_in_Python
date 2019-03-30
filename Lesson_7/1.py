"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

import random
import timeit

a = [random.randint(-100, 100) for i in range(40)]
print(a)


# Вариант №1
def bubble_sort(a):
    for j in range(len(a)):
        for i in range(len(a)-1):
            if a[i] < a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]

    return a


# Вариант №2 (Оптимизированый)
def bubble_sort2(a):
    j = len(a) - 1
    is_not_ordered = True
    while is_not_ordered:
        is_not_ordered = False
        for i in range(0, j):
            if a[i] < a[i+1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                is_not_ordered = True

        j -= 1

    return a


if __name__ == "__main__":
    print(bubble_sort(a))
    print(bubble_sort2(a))
    print(timeit.timeit("bubble_sort(a)", setup="from __main__ import bubble_sort, a", number=1000))
    print(timeit.timeit("bubble_sort2(a)", setup="from __main__ import bubble_sort2, a", number=1000))
