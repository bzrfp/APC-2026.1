#Elabore um programa que recebe uma string e retorna os caracteres contidos nos índices ímpares dessa string,
#ignorando os espaços em branco

s = input()
sfinal = ""
index = -1

for i in range (len(s)):
    
    index += 1
    
    if (index+1)%2 == 0 and s[index] != " ":
        
        sfinal = sfinal + s[index]
        
print(sfinal)
