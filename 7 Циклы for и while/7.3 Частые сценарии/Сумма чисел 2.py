num = int(input())
a = 0
for i in range(1, num + 1):
    b = i ** 2
    if b % 10 == 2 or b % 10 == 5 or b % 10 == 8:
        a += i
print(a)
