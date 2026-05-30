t_atletas, empresarios, t_equipes = map(int, input().split())
equipe_do_atleta = list(map(int, input().split()))
total_atleta_por_empresario = list(map(int, input().split()))

empresarios_suspeitos = []

for i in range (empresarios):
    
    equipes_agenciadas = []
    atletas_agenciados = list(map(int, input().split()))
    
    for atleta in atletas_agenciados:
        
        if equipe_do_atleta[atleta-1] not in equipes_agenciadas:
        
            equipes_agenciadas.append(equipe_do_atleta[atleta-1])
            
    if len(equipes_agenciadas) == t_equipes:
        
        empresarios_suspeitos.append(i+1)
        
if empresarios_suspeitos == []:
    print("-1")
else:
    empresarios_suspeitos.sort()
    print(*empresarios_suspeitos)
