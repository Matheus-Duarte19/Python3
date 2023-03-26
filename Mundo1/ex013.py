salário = float(input('Qual é o salário do Funcionário? R$'))
novo = salário + (salário * 15 / 100) 
print('Um funcionário que ganhava R${:.2f}, com 155 de aumento, passa a recerber R${:.2f}'.format(salário, novo))