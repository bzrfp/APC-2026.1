#Votação

chapa_um, num_um = input().split()
chapa_dois, num_dois = input().split()
chapa_tres, num_tres = input().split()

soma_um = 0
soma_dois = 0
soma_tres = 0


#conta os votos 
while True:
    
    voto = input()
    
    if voto == num_um:
        soma_um += 1
        
    elif voto == num_dois:
        soma_dois += 1
        
    elif voto == num_tres:
        soma_tres += 1
    
    elif voto == '':
        break
    
#imprime o resultado     
if soma_um > soma_dois and soma_um > soma_tres:
    
    print(f"{chapa_um} venceu com {soma_um} votos!")
    
elif soma_dois > soma_um and soma_dois > soma_tres:
    
    print(f"{chapa_dois} venceu com {soma_dois} votos!")
    
elif soma_tres > soma_um and soma_tres > soma_dois:
    
    print(f"{chapa_tres} venceu com {soma_tres} votos!")
    
elif soma_um == soma_dois and soma_dois == soma_tres:
    
    print("Empate, entre as 3 chapas...")
    
elif soma_um == soma_dois or soma_dois == soma_tres or soma_um == soma_tres:
    
    print("Empate, entre 2 chapas...") 
