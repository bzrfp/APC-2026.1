def stockmarket(stock):
    
    d = {}
    
    for i in stock:
        
        if i[0] in d:
            d[i[0]] += float(i[1]*i[2])
        else:
            d[i[0]] = float(i[1]*i[2])
    
    return d
