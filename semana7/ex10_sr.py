#avalia filme sem retorno
def nota(n):
    
    estrela_p = n*"★"
    estrela_t = (10-n)*"☆"
    
    total = f"|{estrela_p}{estrela_t}|"
    
    print (total)
    
n = int(input())
nota (n)
