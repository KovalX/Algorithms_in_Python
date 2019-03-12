"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""


def reverse_number(num, c=0):
    if num != 0:
        if num % 10 == number:
            c += 1
        num = num // 10
        reverse_number(num, c)
    else:
        print("Цифра {} повторяется {} раз(а)".format(number, c))


number = int(input("Введите цифру которую необходимо посчитать: "))
quantity = int(input("Количество вводимых чисел: "))


for i in range(quantity):
    reverse_number(int(input()))




