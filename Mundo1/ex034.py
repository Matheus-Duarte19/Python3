salario = float(input("Digite o salário atual do funcionário: R$"))

if salario >= 1250:
    aumento = salario * 0.1
else:
    aumento = salario * 0.15

novo_salario = salario + aumento

print("O salário atual é: R$ {:.2f}".format(salario))
print("O aumento salarial é: R$ {:.2f}".format(aumento))
print("O novo salário é: R$ {:.2f}".format(novo_salario))
