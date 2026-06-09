def controle(n, c):
    
    if c >= 1 and c < n:
        print(f"Voce ja tomou {c} comprimidos, restam {n-c}.")
    
    if c < n:
        controle(n, c+1)
    elif c == n:
        print (f"Parabens Julie! Voce tomou todos os {n} comprimidos!")
