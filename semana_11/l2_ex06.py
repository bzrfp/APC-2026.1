num_lojas, mangos, rodadas = map(int, input().split())

qtd_prod_lojas = list(input().split())

soma = 0
lista_produtos = []
falhou = False

for i in range (num_lojas):
    precos = list(map(int, input().split()))
    precos.sort()
    lista_produtos.append(precos)

for j in range (rodadas):
    
    for k in range(num_lojas):
        
        if lista_produtos[k] != []:
            preco_minimo = lista_produtos[k][0]
        
            soma += preco_minimo
        
            lista_produtos[k].pop(0)
            
        else:
            falhou = True
            break
        
if soma <= mangos and falhou == False:
    print("Sim")
    
else:
    print("Nao")
