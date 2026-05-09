l = int(input())

combustivel = l
km = 0
falhou = False

while True:
    
    tipo = int(input())
    
    if tipo == -1:
        break
    
    elif tipo == 0:
        if combustivel > 0:
            km += 1
            combustivel -= 1
        else:
            falhou = True
        
    elif tipo == 1:
        x = int(input())
        if combustivel >= 0:
            km += 1
            combustivel = combustivel + x
            if combustivel > l:
                combustivel = l
        else:
            falhou = True
    
    elif tipo == 2:
        y = int(input())
        combustivel -= y
        if combustivel >= 0:
            km += 1
        else:
            falhou = True
            
    print(f"km: {km}")
    print(f"c: {combustivel}")
            

if falhou:
    print(km)
else:
    print('Lar Deivis lar')
