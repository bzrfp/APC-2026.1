#ex fixacao, recibo simples
p, q, v = input().split()

q = int(q)
v = float(v)

total = q*v

print(f"Produto : {p} Qtd. : {q} Unitário: R$ {v:.2f} Total : R$ {total:.2f}")
