def cadastrar_alunos_em_turmas(lista_alunos):
    cadastro_turmas = {}
    
    for aluno in lista_alunos:
        
        t = (aluno["matricula"], aluno["nome"])
        turma = aluno["curso"]
        
        cadastro_turmas[t] = turma
        
    return (cadastro_turmas)
