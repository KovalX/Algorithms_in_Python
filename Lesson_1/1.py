# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

n = int(input("Введите трехзначное число: "))
print("Сумма: ", n // 100 + (n % 100 // 10) + n % 10)
print("Произведение: ", n // 100 * (n % 100 // 10) * (n % 10))
