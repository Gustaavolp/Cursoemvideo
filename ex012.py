#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço = float(input('Digite o preço de seu produto R$:'))
print('O novo valor de seu produto de R$:{:.2f} com desconto de 5% sera de R$:{:.2f}'.format(preço, preço-(preço*5/100)))
