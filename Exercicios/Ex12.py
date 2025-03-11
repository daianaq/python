import math

def equacao(a, b, c):
    if a == 0:
        print("A variável 'A' deve ser diferente de zero")
        return

    delta = b**2 - 4*a*c

    if delta < 0:
        print(f"Delta = {delta}. Não existem raízes reais.")
    
    elif delta == 0:
        x = -b / (2*a)
        print(f"Delta = 0, existe uma raiz real: {x}")
    
    else:
        raiz_delta = math.sqrt(delta)
        xUm = (-b + raiz_delta) / (2*a)
        xDois = (-b - raiz_delta) / (2*a)
        print(f"Delta = {delta}, existem duas raízes reais: {xUm} e {xDois}")

a = float(input("Informe o valor de A: "))
b = float(input("Informe o valor de B: "))
c = float(input("Informe o valor de C: "))

equacao(a, b, c)