#solucao semana 4 
valor =  float(input())
cents = valor*100

#Cédulas
ced_100 = cents//10000
cents %= 10000

ced_50 = cents//5000
cents %= 5000

ced_20 = cents//2000
cents %= 2000

ced_10 = cents//1000
cents %= 1000

ced_5 = cents//500
cents %= 500

ced_2 = cents//200
cents %= 200

#Moedas
mod_100 = cents//100
cents %= 100

mod_50 = cents//50
cents %= 50

mod_25 = cents//25
cents %= 25

mod_10 = cents//10
cents %= 10

mod_05 = cents//5
cents %= 5

mod_01 = cents

print("NOTAS:")

print(f"{int(ced_100)} nota(s) de R$ 100.00")
print(f"{int(ced_50)} nota(s) de R$ 50.00")
print(f"{int(ced_20)} nota(s) de R$ 20.00")
print(f"{int(ced_10)} nota(s) de R$ 10.00")
print(f"{int(ced_5)} nota(s) de R$ 5.00")
print(f"{int(ced_2)} nota(s) de R$ 2.00")

print("MOEDAS:")

print(f"{int(mod_100)} moeda(s) de R$ 1.00")
print(f"{int(mod_50)} moeda(s) de R$ 0.50")
print(f"{int(mod_25)} moeda(s) de R$ 0.25")
print(f"{int(mod_10)} moeda(s) de R$ 0.10")
print(f"{int(mod_05)} moeda(s) de R$ 0.05")
print(f"{int(mod_01)} moeda(s) de R$ 0.01")
