#A lista contém o nome do colaborador e o seu salário base em reais, separados por uma vírgula, um por linha. 
#A lista tem um tamanho dado N.

#Elabore um programa que imprima um relatório com a média salarial da empresa,
#o nome do colaborador com o maior salário e o seu salário, 
#o nome do colaborador com o menor salário e o seu salário.


n = int(input())
sal_maior = 0
sal_menor =  1000000000
soma = 0

if n == 0:
    
    print("Não tem média")
    print("Não tem")
    print("Não tem")
    
else:

    for i in range (n):
    
        nome, sal = input().split(",")
    
        sal = float(sal)
    
        soma += sal 
    
        if sal > sal_maior:
    
            sal_maior = sal
        
            melhor_pago = nome
        
        if sal < sal_menor:
        
            sal_menor = sal
        
            pior_pago = nome
        
        
    media = soma/n

    print(f"{media:.2f}")
    print(f"{melhor_pago} {sal_maior:.2f}")
    print(f"{pior_pago} {sal_menor:.2f}")
