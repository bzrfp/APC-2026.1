pa, pb, t1, t2 = input().split()

ano = 0 

pa = int(pa)
pb = int(pb)

t1 = float(t1)
t2 = float(t2)

if t2 > t1:
    print("A nunca alcancara B.")
    
else:

    while True:
    
        ano += 1 
    
        pa = pa + pa*t1//100
        pb = pb + pb*t2//100
    
        if pa >= pb:
            break

    if ano > 1000:
        print("Mais de um milenio.")
    else:
        print(f"Vai alcancar em {ano} ano(s).")
