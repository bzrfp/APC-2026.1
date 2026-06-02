#conta a frequencia de "d"s, "t"s e "v"s na frase
frase = input()

freq = {}

for i in range (len(frase)):
    if frase[i] == "d":
        if "d" in freq:
            freq["d"] += 1
        else:
            freq["d"] = 1
            
    elif frase[i] == "t":
        if "t" in freq:
            freq["t"] += 1
        else:
            freq["t"] = 1
            
    elif frase[i] == "v":
        if "v" in freq:
            freq["v"] += 1
        else:
            freq["v"] = 1
            
if "d" in freq: 
    d = freq["d"]
    print(f"d {d}")
    
if "t" in freq:
    t = freq["t"]
    print(f"t {t}")
    
if "v" in freq:
    v = freq["v"]
    print(f"v {v}")
