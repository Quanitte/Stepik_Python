num = int(input())
max_n, min_n = 0, 9
while num != 0:
    if max_n < num % 10:
        max_n = num % 10
    if min_n > num % 10:
        min_n = num % 10
    num //= 10
print(f'Максимальная цифра равна {max_n}', f'Минимальная цифра равна {min_n}', sep='\n')