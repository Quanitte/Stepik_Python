num = int(input())
ma, mi = 0, 9
while num > 0:
    if ma < num % 10:
        ma = num % 10
    if mi > num % 10:
        mi = num % 10
    num //= 10
if mi == ma:
    print('YES')
else:
    print('NO')