n, i = map(int, input().split())

n0 = 0
soma = 0

while (n0 < n):
    
    n0 = n0 + 1
    
    a = int(input())
    soma += a
    
print(f"media: {soma//n}") 
    
if (soma//n >= i):
    print("o rock reinara mais uma vez")
else:
    print("rockeiros trabalhando ja")
