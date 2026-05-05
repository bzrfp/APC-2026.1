nome, ano_zero, mat, ano_atual = input().split()

ano_zero_ano, ano_zero_sem = map(int, ano_zero.split("."))

ano_atual_ano, ano_atual_sem = map(int, ano_atual.split("."))

total_anos = ano_atual_ano - ano_zero_ano

total_sem = total_anos*2 + (ano_atual_sem - ano_zero_sem)


if (total_sem > 10):
    
    mat = int(mat)
    
    if (mat%2 == 0):
        cor = "clara"
        
    else:
        cor = "escura"
    
    print (f"Esta pessoa agora é um gato do ICC Norte de cor {cor}.")
    
else :
    
    sem_restantes = 10 - total_sem
    
    print(f"Ufa, ele ainda não virou um gato. Aproveite esse(s) {sem_restantes} semestre(s)!")

