# Verifique se a string lida vira (ou continua sendo) um palíndromo caso exatamente 1 caractere seja trocado

def acha_inverso(s):
    
    s_inverso = ""
    index = -1
    
    for i in range (len(s)):
    
        s_inverso = s_inverso + s[index]
    
        index -= 1
    
    return(s_inverso)


def acha_char_diferentes(s):
    
    soma = 0
    index = -1
    
    acha_inverso(s) 
    
    s_inverso = acha_inverso(s)
    
    for i in range (len(s)):
        
        index += 1
        
        if s[index] != s_inverso[index]:
            soma += 1
            
    return soma    

s = input()

status = "" 

acha_inverso(s) 
    
if acha_inverso(s) == s and len(s)%2 != 0:
    status = "ON"
    
elif acha_inverso(s) == s and len(s)%2 == 0:
    status = "OFF"
    
else:
    
    acha_char_diferentes(s)
    
    if acha_char_diferentes(s) == 2:
        status = "ON"
        
    else:
        status = "OFF" 
    
print(status)
