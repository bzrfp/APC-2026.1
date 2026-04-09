#este problema é similar ao ex06 da S2
#resolução realizada durante a semana 4 

i = int(input())

a = i//365
m = (i%365)//30
d = i - a*365 - m*30

print (f"{a} ano(s)")
print (f"{m} mes(es)")
print (f"{d} dia(s)")
