#Calcula a diferença do tempo maximo do corredor pra cada volta 
n = int(input())
l = list(map(int, input().split()))

tmax = max(l)

resp = []

for i in l:
    dif = tmax - i
    resp.append(dif)
    
print(*resp)
