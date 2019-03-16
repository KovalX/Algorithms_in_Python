# 4.	Определить, какое число в массиве встречается чаще всего.

a = [8, 6, 21, 17, 4, 8, 3, 13, 17, 4, 5, 96, 3, 11, 4, 8]

num = None
n = 0

for i in range(len(a)):
    if a.count(a[i]) > n:
        n = a.count(a[i])
        num = a[i]

print(num)
