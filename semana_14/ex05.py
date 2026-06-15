def positivo(a): 
    if a < 0:
        print("Que negatividade...")
        positivo(int(input()))
    else:
        print("Viva a positividade!")
        
positivo(int(input()))
