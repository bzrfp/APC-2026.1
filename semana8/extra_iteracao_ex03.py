n = int(input())
problemas = 0

for i in range(n):

    a, b, c = map(int, input().split())

    if a+b+c >= 2:
        problemas += 1
    
print(problemas)
