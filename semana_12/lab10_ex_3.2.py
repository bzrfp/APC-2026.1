def calcular_medias_turma(turma):
    for aluno in turma:
        media = sum(aluno["notas"])/len(aluno["notas"])
        aluno["media_final"] = media
    
    print(*turma_dados)
