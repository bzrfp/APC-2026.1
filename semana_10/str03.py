# Elabore um programa que recebe uma string e retorna a quantidade de dígitos numéricos contidas nela.

s = input()

soma = 0
index = -1 

for i in range (len(s)):
    
    index += 1
    
    if s[index] == "0" or s[index] == "1" or s[index] == "2" or s[index] == "3" or s[index] == "4" or s[index] == "5" or s[index] == "6" or s[index] == "7" or s[index] == "8" or s[index] == "9":
        soma += 1
        

print (soma)
