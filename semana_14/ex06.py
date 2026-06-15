def paresDeNumeros(n, m):
    if n <= m:
        print(n, m)
        paresDeNumeros(n+1, m-1)
