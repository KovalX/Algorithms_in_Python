"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

max_sum = 0
max_number = 0

user_number = None

print("Введите натуральные числа. Для нахождения наибольшего числа по сумме цифр введите 0")
while user_number != 0:
    s = 0
    user_number = int(input())
    n = user_number
    while n != 0:
        s += n %10
        n = n // 10
    if s > max_sum:
        max_sum = s
        max_number = user_number

print("Наибольшее число по сумме цифр: {}. Сумма цифр этого числа: {}".format(max_number, max_sum))



