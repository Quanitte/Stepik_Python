true = True
for i in range(10):
    a = int(input())
    if a % 2 == 0:
        continue
    elif a % 2 != 0:
        true = False
if true == True:
    print('YES')
elif true == False:
    print('NO')