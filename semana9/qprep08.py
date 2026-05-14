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
suposto_checksum = int(input ())

checksum = calcular_checksum(mensagem)

if checksum == suposto_checksum:
    print("Transmissao OK.")
    
else:
    print("Erro na transmissao!")
