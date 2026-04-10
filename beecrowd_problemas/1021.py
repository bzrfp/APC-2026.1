#solução semana 4 
#Algum teste ainda está dando erro 
valor =  float(input())

#Cédulas
ced_100 = valor//100
ced_50 = (valor%100)//50
ced_20 = ((valor%100)%50)//20
ced_10 = (((valor%100)%50)%20)//10
ced_5 = ((((valor%100)%50)%20)%10)//5
ced_2 = (((((valor%100)%50)%20)%10)%5)//2

menor_que_dois = ((((((valor%100)%50)%20)%10)%5)%2)

#Moedas
mod_100 = menor_que_dois//1
mod_50 = (menor_que_dois - mod_100)//0.5
mod_25 = (menor_que_dois - mod_100 - 0.5*mod_50)//0.25
mod_10 = (menor_que_dois - mod_100 - 0.5*mod_50 - 0.25*mod_25)//0.1
mod_05 = (menor_que_dois - mod_100 - 0.5*mod_50 - 0.25*mod_25 - 0.1*mod_10)//0.05
mod_01 = (menor_que_dois - mod_100 - 0.5*mod_50 - 0.25*mod_25 - 0.1*mod_10 - 0.05*mod_05)//0.01

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
