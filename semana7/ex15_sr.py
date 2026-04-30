#define as moedas necessarias para devolver o troco
def troco (x):
    
    m50 = x//50
    x %= 50
    
    m25 = x//25
    x %= 25
    
    m10 = x//10
    x %= 10
    
    m05 = x//5
    x %= 5
    
    m01 = x
    
    print(f"{m50} moedas de 50 centavos")
    print(f"{m25} moedas de 25 centavos")
    print(f"{m10} moedas de 10 centavos")
    print(f"{m05} moedas de cinco centavos")
    print(f"{m01} moedas de 1 centavo")
