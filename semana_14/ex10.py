#Verifica se tem elementos repetidos na lista 
l = list(map(int, input().split()))
ja_tem = []

b = False

for i in  l:
    if i in ja_tem:
        b = True
    else:
        ja_tem.append(i)

print(b)
