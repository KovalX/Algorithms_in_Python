"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""


def reverse_number(num):
    if num != 0:
        print(num % 10, end="")
        num = num // 10
        reverse_number(num)


reverse_number(int(input()))
