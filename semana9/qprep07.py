def calcular_soma(mensagem):

    n = len(mensagem)

    soma = 0 

    for i in range (n):
        soma = soma + ord(mensagem[i])
        
    return soma 
    
def calcular_checksum(mensagem):
    
    soma = calcular_soma(mensagem)
    
    checksum = soma%256
    
    return checksum


mensagem = input()
tamanho = int(input())

n = len(mensagem)

x = 0 

for i in range (0, n, tamanho):
    
    x += 1 
    
    pacote = mensagem[i:i+tamanho]
    
    checksum = calcular_checksum(pacote) 
    
    print (f"Pacote {x}: [{pacote}] | Checksum: {checksum} ")
    
    
print (f"Total de pacotes: {x}")
