#calculo da Media 3 
#solucao semana 5

a, b, c, d = map(float, input().split())

mp = (a*2+b*3+c*4+d)/10

print(f'Media: {mp:.1f}')

if (mp >= 7):
    print('Aluno aprovado.')
    
elif (mp < 5):
    print('Aluno reprovado.')
    
else:
    print('Aluno em exame.')
    
    ne = float(input())
    
    mf = (mp+ne)/2
    
    print(f'Nota do exame: {ne:.1f}')
    
    if (mf >= 5):
        print('Aluno aprovado.')
        
    else:
        print('Aluno reprovado.')
        
    print(f'Media final: {mf:.1f}')
