#Corrija a função que retorna True caso a palavra nao possua a letra u
def não_possui_a_letra_u(palavra):
    
    if "u" in palavra or "U" in palavra: 
        return False 
    elif "ú" in palavra or "Ú" in palavra: 
        return False
    elif "ü" in palavra or "Ü" in palavra: 
        return False 
    elif "û" in palavra or "Û" in palavra: 
        return False 
    elif "ù" in palavra or "Ù" in palavra: 
        return False 
    else: 
        return True
