n, m = map(int, input().split())

l = list(map(int, input().split()))

for i in range (m):
    index, cons = map(int, input().split())
    
    l[index] = cons
    print(l)
