"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""

import random


# Вариант №1
m = random.randint(0, 10)
a = [random.randint(0, 100) for i in range(2 * m + 1)]
print(a)

for i in range(m):
    a.remove(min(a))

print("Медиана: ", min(a))


"""
# Вариант №2. Поразрядная сортировка
def sort_func(a):
    length = len(str(max(a)))
    rang = 10
    for i in range(length):
        b = [[] for k in range(rang)]
        for x in a:
            figure = x // 10**i % 10
            b[figure].append(x)
        a = []
        for k in range(rang):
            a = a + b[k]
    return a


m = random.randint(0, 10)
a = [random.randint(0, 100) for i in range(2 * m + 1)]
print(a)
a = sort_func(a)
print("Отсортированный список: ", a)
print("Медиана:", a[len(a) // 2])
"""