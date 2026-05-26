#leia n orações e adicione o sujeito "Raimundo Nonato" no ínicio de cada uma delas

n = int(input())
l =[]

for i in range (n):
    periodo = input()
    l.append(periodo)
    
for i in range (n):
    print(f"Raimundo Nonato {l[i]}")
