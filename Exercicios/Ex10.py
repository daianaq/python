x = int(input("Informe o 1º comprimento:"))
y = int(input("Informe o 2º comprimento:"))
z = int(input("Informe o 3º comprimento:"))

if (x+y>z) and (x+z>y) and (y+z>x):
    if (x==y==z):
        print("É um triângulo equilátero.")
    elif (x==y) or (x==z) or (y==z):
        print("É um triângulo isósceles.")
    else:
        print("É um triângulo escaleno.")
else:
    print("Os valores não formam um triângulo.")
    
    