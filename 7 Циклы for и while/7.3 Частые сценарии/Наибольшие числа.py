num = int(input())
max1, max2 = 0, 0
for i in range(num):
    num = int(input())
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        max2 = num
print(max1, max2, sep='\n')