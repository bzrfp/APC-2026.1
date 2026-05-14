#define função calcular_soma e calcular_checksum 

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
