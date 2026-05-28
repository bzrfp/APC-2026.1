#Faça um programa que receba os nomes dos alunos e organize os nomes dos alunos de acordo com a ordem alfabética inversa. 
#A saída será a quantidade de alunos e uma lista contendo os nomes dos alunos em ordem alfabética inversa.
chamada = []
total = 0

while True:
    nome = input()
    
    if nome == "EOF":
        break
    else:
        chamada.append(nome)
        total += 1
        
chamada.sort(reverse=True)
        
print(total)
print(chamada)
