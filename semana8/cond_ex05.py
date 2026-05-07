#rascunho

dia_inicio = input()
horario_inicio = input()

dia_fim = input()
horario_fim = input()

dia_inicio_string, dia_inicio_num = dia_inicio.split()

dia_inicio_num = int(dia_inicio_num)


dia_fim_string, dia_fim_num = dia_fim.split()

dia_fim_num = int(dia_fim_num)


hora_inicio, min_inicio, seg_inicio = map(int, horario_inicio.split(" : "))

hora_fim, min_fim, seg_fim = map(int, horario_fim.split(" : "))


t_dias = dia_fim_num - dia_inicio_num
t_horas = hora_fim - hora_inicio
t_min = min_fim - min_inicio
t_seg = seg_fim - seg_inicio 
