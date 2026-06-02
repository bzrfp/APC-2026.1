def contar_frequencia(texto):
    
    textop = texto.upper()
    l = textop.split()
    d = {}
    
    for palavra in l:
        if palavra in d:
            d[palavra] += 1
        else:
            d[palavra] = 1
            
    return d
