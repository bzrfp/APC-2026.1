#Elabore um programa que recebe como entrada um tweet e a palavra a ser censurada, 
#caso a palavra a ser censurada esteja no tweet, imprima-o com a censura, caso contrário imprima "tudo certo :)". 

s = input()
palavra = input()

if palavra in s:
    
    print(s.replace(palavra, "*"))
    
else:
    
    print("tudo certo :)") 
