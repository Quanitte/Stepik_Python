num = int(input())
n1_1, n1, n2, n3, n4, n5, n6 = num, 0, 0, 1, 0, 0, 0

while n1_1 > 0:
    n1 += n1_1 % 10
    n2 += 1
    n3 *= n1_1 % 10
    n4 = n1 / n2
    n5 = (num // (10 ** (n2 - 1)))
    n6 = (num % 10) + (num // (10 ** (n2 - 1)))
    n1_1 //= 10
    
print(n1, n2, n3, n4, n5, n6, sep='\n')
