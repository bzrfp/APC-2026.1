n = int(input())

nomes = {}

for i in range (n):
    
    emails = {}
    
    aluno = list(input().split())
  
    notas = list(map(float, aluno[2:]))
    
    media = sum(notas)/len(notas)
  
    emails[aluno[1]] = media
  
    nomes[aluno[0]] = emails

dest = input()

if dest not in nomes:
    print(f"O aluno {dest} não está na turma.") 
else:
    
    email_aluno = list(nomes[dest].keys())[0]
    
    print(f"Destinatário: {email_aluno}")
    
    media_final = nomes[dest][email_aluno]
    
    if media_final >= 4.995:
    
        print(f"O aluno {dest} foi aprovado com média {media_final:.2f}.")
        
    else:
        
        print(f"O aluno {dest} foi reprovado com média {media_final:.2f}.")
