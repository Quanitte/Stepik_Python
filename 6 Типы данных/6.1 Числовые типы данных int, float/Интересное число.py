a = int(input())
if abs(a // 100 - a % 10) == (a // 10) % 10 or a // 100 + a % 10 == (a // 10) % 10:
    print('Число интересное')
else:
    print('Число неинтересное')