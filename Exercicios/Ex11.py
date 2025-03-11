altura = float(input("Digite a altura da pessoa (em metros): "))
peso = float(input("Digite o peso da pessoa (em kg): "))

if altura < 1.20:
    if peso <= 60:
        classificacao = "Classificação: A"
    elif 60 < peso <= 90:
        classificacao = "Classificação: D"
    else:
        classificacao = "Classificação: G"
elif 1.20 <= altura <= 1.70:
    if peso <= 60:
        classificacao = "Classificação: B"
    elif 60 < peso <= 90:
        classificacao = "Classificação: E"
    else:
        classificacao = "Classificação: H"
elif altura > 1.70:
    if peso <= 60:
        classificacao = "Classificação: C"
    elif 60 < peso <= 90:
        classificacao = "Classificação: F"
    else:
        classificacao = "Classificação: I"

print(classificacao)