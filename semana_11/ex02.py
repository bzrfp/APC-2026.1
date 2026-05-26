#ao receber uma lista de inteiros, soma-se o primeiro elemento multiplicado por 2 ao segundo elemento multiplicado por 1/2. 
#Com este resultado, multiplica-se por 2 e faz a soma com o terceiro elemento da lista multiplicado por 1/2 e assim sucessivamente

l = list(map(int, input().split()))

soma = 0
i = 0 

while i+1 < len(l):
    
    if i == 0:
        soma = l[i]*2 + l[i+1]*1/2
    else:
        soma = soma*2 + l[i+1]*1/2
        
    i += 1
        
print(f"{soma:.2f}")
