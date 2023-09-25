a, b, c = int(input()), int(input()), int(input())
days = 1
for i in range(c):
    print(days, a * (b / 100 + 1) ** i)
    days += 1