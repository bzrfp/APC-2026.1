#ex. fixacao, calc. imc
p, a = map(float, input().split())

imc = p/(a**2)

print(f"IMC: {imc:.2f}")
