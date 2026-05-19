#Descompressao de strings

n = int(input())

for i in range(n):

    s = input()
    index = 0

    while index < len(s):

        letra = s[index]
        index += 1

        num = ""

        while index < len(s) and s[index].isdigit():

            num = num + s[index]
            index += 1

        num = int(num)

        print(letra * num, end = "")
    
    print() 
