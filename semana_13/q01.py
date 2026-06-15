# criar uma função recursiva escada que recebe como parâmetro um número n e imprima uma escada com n degraus
def escada(n):
    if n == 0:
        return
    else:
        escada(n-1)
        print("#"*n)
