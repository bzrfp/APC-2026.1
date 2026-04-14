#Dado dois números inteiros de entrada que são a base e a altura de um triângulo
#mostre o valor da área com duas casas decimais
base  = int(input())
altura = int(input())
area = (base * altura)/2
print(f'{area:.2f}')
