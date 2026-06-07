#Encontre os alunos que tiveram a mesma nota que o usuário

def busca_reversa(d, v):
    
    mesma_nota = []
    
    for chave in d:
        if d[chave] == v:
            mesma_nota.append(chave)
    
    return mesma_nota

n = int(input())

d = {}

for i in range (n):
    nome, nota = input().split(",")
    nota = float(nota)
    
    d[nome] = nota
    
minha_nota = float(input())

mesma_nota = busca_reversa(d, minha_nota)
mesma_nota.sort()


if mesma_nota == []:
    print("Você foi o único aluno com essa nota.")
else:
    
    s = ""
    for i in range (len(mesma_nota)):
        if i == 0:
            s += mesma_nota[i]
        else:
            s += "/"
            s += mesma_nota[i]
    
    print(s)
