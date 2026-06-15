d = {}

while True:
    
    s = input()
    n = input()
    
    if s == "fim":
        chave_escolhida = n 
        break
    
    d[s] = n

v = list(map(int, d.values()))

print(sum(v))

if chave_escolhida not in d:
    print("Essa chave não existe no dicionário")
else:
    d.pop(chave_escolhida)
    nv = list(map(int, d.values()))
    print(sum(nv))
