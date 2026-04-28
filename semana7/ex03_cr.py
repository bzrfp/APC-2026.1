def avaliaFilme(nota):
    
    estrela_preta = nota*"★"
    estrela_t = (10-nota)*"☆"
    
    total = f"|{estrela_preta}{estrela_t}|"
    
    return total
