total = 0
num = int(input())
for i in range(1, num + 1):
    if num % i == 0:
        total += i
print(total)