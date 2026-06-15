def ainda_faltam(n):
    if n > 1:
        if n == 5:
            print("Seu tempo está acabando!")    
        else:
            print(f"Atenção faltam {n} segundos...")
        ainda_faltam(n-1)
    
n = int(input())
p = int(input())

if n == 0:
    print("Cabum!!!! Explodiu")
else:
    if p < n:
        ainda_faltam(n)
        print("Seja rápido. Falta 1 segundo")
        print("Cabum!!!! Explodiu")
    else:
        ainda_faltam(n)
        print("Bomba desativada automaticamente!")
