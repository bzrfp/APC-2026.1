#resolução realizada durante a semana 4 

valor =  int(input())

cedcem = valor//100
cedcinq = (valor%100)//50
cedvinte = ((valor%100)%50)//20
ceddez = (((valor%100)%50)%20)//10
cedcinc = ((((valor%100)%50)%20)%10)//5
ceddois = (((((valor%100)%50)%20)%10)%5)//2
cedum = ((((((valor%100)%50)%20)%10)%5)%2)

print(valor)

print(f"{cedcem} nota(s) de R$ 100,00")
print(f"{cedcinq} nota(s) de R$ 50,00")
print(f"{cedvinte} nota(s) de R$ 20,00")
print(f"{ceddez} nota(s) de R$ 10,00")
print(f"{cedcinc} nota(s) de R$ 5,00")
print(f"{ceddois} nota(s) de R$ 2,00")
print(f"{cedum} nota(s) de R$ 1,00")
