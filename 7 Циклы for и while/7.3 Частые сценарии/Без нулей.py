total = 1
for i in range(10):
    num = int(input())
    if num == 0:
        continue
    else:
        total *= num
print(total)