word = input()
total = 0
while True:
    if word == 'достаточно' or word == 'хватит' or word == 'стоп':
        break
    word = input()
    total += 1
print(total)