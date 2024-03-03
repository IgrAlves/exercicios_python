x = int(input("Digite um numero: "))
cont = 0
while x != 0:
    x = x // 10
    cont = cont + 1
print(cont)