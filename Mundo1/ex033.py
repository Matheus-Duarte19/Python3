num1 = float(input("Primeiro valor: "))
num2 = float(input("Segundo valor: "))
num3 = float(input("Terceiro valor: "))

maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print("O maior número é: {}".format(maior))
print("O menor número é: {}".format(menor))
