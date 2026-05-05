def quantosJantam(n, g, f, c):
    
    if (g > f):
        
        conj = g - (g-f)
        
        total = c + conj
        
    elif (g < f):
        
        conj = f - (f-g)
        
        total = c + conj
        
    else:
        
        total = c + g
        
    if (n >= total):
        print(total)
        
    else:
        print(n)
