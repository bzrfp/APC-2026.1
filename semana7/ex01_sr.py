def exibir_recomendacao(peso):
    
    agua = peso*0.035
    
    print (f"Recomendação: {agua:.2f} litros")
    
    
peso = float(input())
exibir_recomendacao(peso)
