"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""

import random
import timeit


def merge_sort(array):
    if len(array) > 1:
        midpoint = len(array) // 2
        left = array[:midpoint]
        right = array[midpoint:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
        return array


a = [random.randint(0, 50) for i in range(30)]
print(a)

if __name__ == "__main__":
    print(merge_sort(a))
    print(timeit.timeit("merge_sort(a)", setup="from __main__ import merge_sort, a", number=1000))
