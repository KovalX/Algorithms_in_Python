"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""


def odd_even(n, even_num=0, odd_num=0):
    if n != 0:
        if (n % 10) % 2 == 0:
            even_num += 1
        else:
            odd_num += 1
        n = n // 10
        odd_even(n, even_num, odd_num)
    else:
        print("Количество четных цифр: ", even_num, "\nКоличество нечетных цифр: ", odd_num)


odd_even(int(input("Введите число: ")))
