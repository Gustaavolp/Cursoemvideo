"""Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""

from datetime import date
maior = 0
menor = 0
anoatual = date.today().year
for p in range(1, 8):
    ano = int(input('Em que ano a {}º pessoa nasceu? '.format(p)))
    if (anoatual - ano) >= 21:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade \n'
      'E também tivemos {} pessoas menores de idade'.format(maior, menor))
