#Elabore um programa que lê três notas de um aluno e o peso de cada nota e apresenta a média final deste aluno
n1, n2, n3 = map(float, input().split())
p1, p2, p3 = map(int, input().split())

mp = (n1*p1 + n2*p2 + n3*p3)/(p1+p2+p3)

print(f"{mp:.6f}")
