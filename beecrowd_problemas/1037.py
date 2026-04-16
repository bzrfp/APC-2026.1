#intervalo
#solucao semana 5 
x = float(input())

if (75 < x <= 100)
    intervalo = 'Intervalo (75,100]'
    
elif (50 < x <= 75):
    intervalo = 'Intervalo (50,75]'
    
elif (25 < x <= 50):
    intervalo = 'Intervalo (25,50]'
    
elif (0 <= x <= 25):
    intervalo = 'Intervalo [0,25]'
    
else:
    intervalo = 'Fora de intervalo'
    
print(intervalo)
