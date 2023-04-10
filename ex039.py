"""Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

from datetime import date

data = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = data - nasc

if idade <= 17:
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, data))
    print('Ainda faltam {} anos para o seu alistamento.'.format(18 - idade))
    print('Seu alistamento será em {}.'.format(nasc + 18))
elif idade == 18:
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, data))
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade > 18:
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, data))
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(nasc + 18))
