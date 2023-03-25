# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

an = float(input('Digite o ângulo que você deseja: '))
print('O angulo de {}° tem o Seno de {:.2f}'.format(an, sin(radians(an))))
print('O angulo de {}° tem o Cosseno de {:.2f}'.format(an, cos(radians(an))))
print('O angulo de {}° tem a Tangente de {:.2f}'.format(an, tan(radians(an))))
