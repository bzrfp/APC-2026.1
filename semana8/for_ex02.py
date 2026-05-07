#Equilibrio das forças 

n = int(input())
x0 = y0 = z0 = 0

for i in range(n):
    x, y, z = map(int, input().split())
    
    x0 += x
    y0 += y
    z0 += z
    
if (x0 == y0 == z0 == 0):
    print ("YES")
else:
    print("NO")
