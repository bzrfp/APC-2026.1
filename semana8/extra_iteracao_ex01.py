n = 1

while n > 0:
    n = int(input())
    
    if n<=0:
        break
    
    if n > 10**9:
        print("isso ai tem cara de loop infinito")
    else:
        print("nossa o programa foi rapido")
