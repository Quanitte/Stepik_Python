a, b, c = int(input()), int(input()), int(input())
print(max(a,b,c),abs((max(a,b,c) + min(a,b,c) - (a + b + c))), min(a,b,c), sep='\n')