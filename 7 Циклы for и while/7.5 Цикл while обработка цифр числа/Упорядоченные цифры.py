num = int(input())
n1 = num % 10
true = True
while num > 0:
    if num % 10 >= n1:
        n1 = num % 10
        num //= 10
        continue
    else:
        true = False
        break
if true == True:
    print('YES')
else:
    print('NO')