#verifique se os números em l são múltiplos de n

l = list(map(int, input().split()))
n = int(input())

resposta = []

for i in range (len(l)):
    
    if (l[i])%n == 0:
        
        resposta.append(l[i])
        
print(*resposta)
