n = int (input())

d = {}

for i in range(n):
    aluno = input().split(":")
    
    nota = float(aluno[1])
    
    if nota >= 5:
        d[aluno[0]] = nota
        
print(d)
