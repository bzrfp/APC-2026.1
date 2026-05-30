#Decodifica uma mensagem cifrada em blocos de 5 caracteres, revertendo as transformações aplicadas durante a criptografia.
s = input()
msg = []

for i in range (0, len(s), 5):
    pacote = s[i:i+5]
        
    msg.append(pacote)
    
msg.reverse()

for j in range (len(msg)):
    if j%2 == 0:
        msg[j] = msg[j][::-1]

frase = "".join(msg)
print(frase)
