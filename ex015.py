# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado,
# a quantidade de dias pelos quais ele foi alugado
# e calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = float(input('Quantos dias o carro foi alugado? '))
km = int(input('Quantos km voce percorreu? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R$:{:.2f}'.format(pago))
