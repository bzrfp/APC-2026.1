#Dada uma postagem qualquer, calcule o tempo necessário para que um adulto médio consiga ler todo seu conteúdo
#Mostre em duas linhas diferentes o pior tempo estimado e o melhor tempo estimado
s = input()

s = len(s)

PC = s/1200
MC = s/1550

print(f"Pior dos casos: {PC:.3f}")
print(f"Melhor dos casos: {MC:.3f}") 
