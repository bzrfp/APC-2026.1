def exibir_media(n1, n2, n3):
    mf = (n1+n2+n3)/3
    print(f"Média final: {mf:.2f}")

n1, n2, n3 = map(float, input().split())
exibir_media(n1, n2, n3) 
