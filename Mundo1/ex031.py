distancia = float(input("Qual a distância da viagem em km? "))

if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45

print("O preço da passagem é: R$ {:.2f}".format(preco))
