total = 0
while True:
    num = int(input())
    if num > 5 or num < 0:
        break
    elif num == 5:
        total += 1
print(total)