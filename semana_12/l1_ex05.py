#Escreva uma função chamada convert que receberá uma lista de tuplas com dois valores, chave e valor,
#e retornará um dicionário, acumulando todos os valores de chaves iguais em uma lista.
def convert(l):
    d = {}
    
    for i in l:
        if i[0] not in d:
            d[i[0]] = []
       
        d[i[0]].append(i[1])
            
    return d
