#dada uma lista a de tamanho n, você deverá responder m consultas. A cada consulta você lerá dois inteiros i,j
#irá mudar a lista na posição i, fazendo a[i]=j e em seguida irá imprimir a lista
n, m = map(int, input().split())

l = list(map(int, input().split()))

for i in range (m):
    index, cons = map(int, input().split())
    
    l[index] = cons
    print(l)
