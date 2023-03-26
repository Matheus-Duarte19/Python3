preço = float(input('Qual é o preço de produto? R$'))
novo = preço - (preço * 5 /100)

preço = float(input('Qual é o preço de produto? R$'))
novo = preço - (preço * 5 /100)

print('O produto que custava R${:.2f}, na promoçõa com descondo de 5% vai custar R${:.2f}'.format(preço, novo))