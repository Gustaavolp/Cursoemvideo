#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Considere US$:1,00 = R$:3,27
rs = float(input('Quantos reais voce tem? R$:'))
print('Com R$:{:.2f} voce pode comprar US$:{:.2f}'.format(rs, rs/3.27))
