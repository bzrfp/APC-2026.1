#Elabore um programa que recebe uma palavra e imprime uma palavra nova derivada desta,
#que é composta pelos dois primeiros caracteres da palavra de entrada com os dois últimos.

s = input()

s1 = s[0] + s[1]

s2 = s[len(s)-2] + s[len(s)-1]

sfinal = s1+s2

print(sfinal)
