x = float(input("Digite seu salário: "))

if x < 500:
    s = x + (x * 0.15)
    print("O salário será: ", s)
elif x <= 100:
    s = x + (x * 0.10)
    print("O salário será: ", s)
else:
    s = x + (x * 0.05)
    print("O salário será: ", s)
    