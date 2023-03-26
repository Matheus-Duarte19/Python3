velocidade = float(input("Digite a velocidade do carro em Km/h: "))
limite_velocidade = 80

if velocidade > limite_velocidade:
    velocidade_acima_limite = velocidade - limite_velocidade
    multa = velocidade_acima_limite * 7
    print(f"Você foi multado em R${multa:.2f} por exceder o limite de velocidade em {velocidade_acima_limite} Km/h.")

print('Tenha um bom dia! Dirija com segurança')