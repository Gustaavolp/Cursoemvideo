#Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salário, com 15% de aumento.
s = float(input('Digite seu salário: '))
print('Seu novo salário será de R$:{:.2f}'.format(s+(s*15/100)))
