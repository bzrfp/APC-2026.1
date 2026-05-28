m, n = map(int, input().split())

max_distancia = 0
for i in range(m):
    fila = list(map(int, input().split()))
    k=0
    while k <  (len(fila)):
        if fila[k] == 0:
            indice_zero = k
            indice_um = len(fila)
            j = k+1
            while j < len(fila):
                if fila[j] == 1:
                    indice_um = j
                    break
                j += 1

            sequencia_zeros = indice_um - indice_zero
            
            if (indice_zero == 0) or (indice_um == len(fila)):
                distancia = sequencia_zeros
            else:
                if sequencia_zeros % 2 == 0:
                    distancia = sequencia_zeros // 2
                else:
                    distancia = sequencia_zeros // 2 + 1
            
            max_distancia = max(distancia, max_distancia)
        k += 1
print (max_distancia)
                
            
