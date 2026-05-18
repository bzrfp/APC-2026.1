#Faça um programa que transforma os números escritos por extenso em algarismos.
#É garantido que os números estão no intervalo [0,9] e sempre são apresentados em letras minúsculas.

s = input()

if "zero" in s: 
    s = s.replace("zero", "0")

if "um" in s:
    s = s.replace("um", "1")
    
if "dois" in s:
    s = s.replace("dois", "2")
    
if "três" in s:
    s = s.replace("três", "3")
    
if "quatro" in s:
    s = s.replace("quatro", "4")
    
if "cinco" in s:
    s = s.replace("cinco", "5")
    
if "seis" in s:
    s = s.replace("seis", "6")
    
if "sete" in s:
    s = s.replace("sete", "7")
    
if "oito" in s:
    s = s.replace("oito", "8")
    
if "nove" in s:
    s = s.replace("nove", "9")
    
print(s) 
