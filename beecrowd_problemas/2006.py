# identificando o chá 
# solucao semana 4

T = int(input()) 
A, B, C, D, E = map(int, input().split()) 

if (A == T): 
    r1 = 1
else:
    r1 = 0
    
if (B == T): 
    r2 = 1
else:
    r2 = 0
    
if (C == T): 
    r3 = 1
else:
    r3 = 0
    
if (D == T): 
    r4 = 1
else:
    r4 = 0
    
if (E == T): 
    r5 = 1
else:
    r5 = 0
    
print(r1+r2+r3+r4+r5)
