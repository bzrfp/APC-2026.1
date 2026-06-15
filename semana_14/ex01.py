n = int(input())
d ={}

for i in range (n):
    
    l = input().split(":")
    
    d[l[0]] = l[1]

for i in d:
    print("{" + f"'{i}': '{d[i]}'" + "}")
    
print(d)
