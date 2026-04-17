#coordenadas de um ponto
#solucao semana 5

x, y = map(float, input().split())

if (x == 0 and y == 0):
    posicao = 'Origem'
    
elif (x == 0):
    posicao = 'Eixo Y'
    
elif (y == 0):
    posicao = 'Eixo X'
    
elif (x > 0 and y > 0):
    posicao = 'Q1'
    
elif (x < 0 and y > 0):
    posicao = 'Q2'
    
elif (x < 0 and y < 0):
    posicao = 'Q3'
    
else:
    posicao = 'Q4'
    
print(posicao)
