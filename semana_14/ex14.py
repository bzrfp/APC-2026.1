d = {'9': 'p', '6': 'b', '5': 's', '7': 't', '0': 'o', '1': 'i'}

prov = ""

s = input()
for i in range (len(s)):
    if s[i] in d:
        prov += d[s[i]]
    else:
        prov += s[i]
        
resp = prov[0].upper()
resp += prov[1:].lower()

if resp[len(resp)-1] != ".":
    resp += "."
    
print(resp)
