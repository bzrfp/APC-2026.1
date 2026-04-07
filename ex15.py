h = int(input("Informe a hora atual (entre 0 e 23): "))
    
if (h < 5):
    saudacao = "boa madrugada!"
elif (h < 12):
    saudacao = "bom dia!"
elif (h < 18):
   saudacao = "boa tarde!"
else:
    saudacao = "boa noite!"
    
print(saudacao)