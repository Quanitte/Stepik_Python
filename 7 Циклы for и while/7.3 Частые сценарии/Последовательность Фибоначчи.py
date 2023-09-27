num = int(input())
total1 = 0
total2 = 1
for _ in range(num):
    total1, total2 = total2, total1 + total2
    print(total1, end=' ') 