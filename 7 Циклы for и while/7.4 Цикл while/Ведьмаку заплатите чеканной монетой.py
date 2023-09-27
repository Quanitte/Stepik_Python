num = int(input())
total = 0
while True:
    if num >= 25:
        total += 1
        num -= 25
    elif num >= 10:
        total += 1
        num -= 10
    elif num >= 5:
        total += 1
        num -= 5
    elif num > 0:
        total += 1
        num -= 1
    else:
        break
print(total)