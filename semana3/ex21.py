usuario = input().strip()

if (usuario == "admin"):
    senha = input().strip()
        
    if (senha == "1234"):
        print("Acesso concedido")
    else:
        print("Senha inválida")
        
else:
    print("Usuário desconhecido")
