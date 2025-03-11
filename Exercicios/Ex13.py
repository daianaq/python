def calcular_preco_grama(codigoProduto):
    if 1 <= codigoProduto <= 4:
        return 10
    elif 5 <= codigoProduto <= 7:
        return 25
    elif 8 <= codigoProduto <= 10:
        return 35
    else:
        return 0

def calcular_imposto(precoTotal, codigoPais):
    if codigoPais == 1:
        return precoTotal * 0.00
    elif codigoPais == 2:
        return precoTotal * 0.15
    elif codigoPais == 3:
        return precoTotal * 0.25
    else:
        return 0

codigoProduto = int(input("Digite o código do produto (1-10): "))
pesoKg = float(input("Digite o peso do produto em quilos: "))
codigoPais = int(input("Digite o código do país de origem (1-3): "))

pesoGramas = pesoKg * 1000
precoGrama = calcular_preco_grama(codigoProduto)
precoTotal = pesoGramas * precoGrama
imposto = calcular_imposto(precoTotal, codigoPais)
valorTotal = precoTotal + imposto

print(f"Peso do produto em gramas: {pesoGramas:.2f}g")
print(f"Preço total do produto: R${precoTotal:.2f}")
print(f"Valor do imposto: R${imposto:.2f}")
print(f"Valor total a pagar (preço + imposto): R${valorTotal:.2f}")
