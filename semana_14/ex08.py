#Album da copa
n = int(input())
m = int(input())

ja_tem = []

for i in range (m):
    
    fig = input()
    
    if fig not in ja_tem:
        ja_tem.append(fig)
        
faltam = n - len(ja_tem)
print(faltam)
