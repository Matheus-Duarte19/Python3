from math import radians, sin, cos, tan
ângulo = float(input('Digite o ângulo que você deseja: '))
an = radians(ângulo)
seno = sin(an)
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = cos(an)
print('O ângulo de {} tem o COSSENO  de {:.2f}'.format(ângulo, cosseno))
tangente = tan(an)
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(ângulo, tangente))