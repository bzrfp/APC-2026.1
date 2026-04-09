operador = input("Informe a operação que deseja realizar (+, -, *, /): ")
   
num1 = float(input("informe o primeiro número: "))
num2 = float(input("informe o segundo número: "))
    
if (operador == "/"):
   
    if (num2 == 0):
        print("Erro: divisão por 0")
    else:
        print("O resultado da operação é: ",  num1 / num2)
                
elif (operador == "+"):
    print("O resultado da operação é: ",  num1 + num2)
            
elif (operador == "-"):
    print("O resultado da operação é: ",  num1 - num2)
            
elif (operador == "*"):
    print("O resultado da operação é: ",   num1 * num2)
            
else:
    print("Erro: operador inválido")
