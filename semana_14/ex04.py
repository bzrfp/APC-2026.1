n = int(input())
d = {}

for i in range (n):
    t, r = input().split("=")
    
    d[t] = r
    
palavra = input()
l = []    

for i in d:
    if d[i] == palavra:
        l. append(i)
        
print(l)
