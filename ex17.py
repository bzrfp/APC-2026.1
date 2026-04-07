altura = float(input("Informe a altura (m): "))
peso = float(input("Informe o peso (kg): "))

imc = peso/(altura*altura)

print ("O imc é ", imc)
    
if (imc < 18.5):
    print("O imc indica que esta pessoa está abaixo do peso")
elif (imc <= 24.9):
    print("O imc indica que esta pessoa está no peso normal")
elif (imc <= 29.9):
    print("O imc indica que esta pessoa está com sobrepeso")
else:
    print("O imc indica que esta pessoa está com obesidade")