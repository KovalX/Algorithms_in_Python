# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

count = 0
for i in range(2, 9):
    for j in range(2, 99):
        if j % i == 0:
            count += 1
    print(count, "чисел кратны цифре", i)
    count = 0
