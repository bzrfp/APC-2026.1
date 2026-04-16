#Leitura de código lanche
#solucao semana 5
x, y = map(int, input().split())

if (x == 1):
    a = 4
    
elif (x == 2):
    a = 4.5
    
elif (x == 3):
    a = 5
    
elif (x == 4):
    a = 2
    
elif (x == 5):
    a = 1.5
    
total = a*y

print (f'Total: R$ {total:.2f}')
