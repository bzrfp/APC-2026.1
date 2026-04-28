#duracao 
#solucao semana 7
h1, h2 = map(int, input().split())

if (h1 == h2):
    th = 24
    
elif (h1 > 12):
    th = (24-h1)+h2
    
else:
    th = h2-h1
    
print(f"O JOGO DUROU {th} HORA(S)")
