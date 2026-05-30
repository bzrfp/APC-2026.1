#crie um algoritmo que receba um vetor de inteiros e retorne o vetor da soma de prefixos desse vetor
def prefix_sum(l):
    
    resp = []
    
    for i in range (len(l)):
        if i == 0:
            resp.append(l[0])
        else:
            soma = sum(resp)
            item = resp[i-1] + l[i]
            resp.append(item)
            
    return resp

l = list(map(int, input().split()))

print(*(prefix_sum(l)))
print(*l)
