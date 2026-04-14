# Escreva um programa que dadas três onomatopeias
# crie uma nova seguindo a lógica entrada: boom zap bang saída: boomzapzapzapbangbang
o1, o2, o3 = input().split()

print(f"{o1+ 3*o2 + 2*o3}")
