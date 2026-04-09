idade = input()
idade = int(idade)

if (idade < 16):
    status = "Não elegível"
elif (idade < 18 or idade > 70):
    status = "Voto Facultativo"
else:
    status = "Voto Obrigatório"
    
print(f"O cidadão possui {idade} anos, portanto seu status é: {status}.")
