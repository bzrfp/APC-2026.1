#verificar se a transmissao pode ser concluida a tempo 

m, t, v = input().split()

m = float(m)
t = int(t)
v = int(v) 

total_bits =  m*1024**2 * 8

bits_max = t*v

if bits_max - total_bits >= 0:
    print("Transmissao concluida a tempo.")

else:
    print("Enlace insuficiente.") 
