#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input('Digite um valor em metros: '))
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(m, m*100, m*1000))
