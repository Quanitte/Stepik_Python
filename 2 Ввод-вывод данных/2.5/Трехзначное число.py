a = int(input())
print(f'Сумма цифр = {(a % 10) + (a // 10 % 10) + a // 100}', f'Произведение цифр = {(a % 10) * (a // 10 % 10) * (a // 100)}', sep='\n')