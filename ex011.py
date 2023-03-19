#Faça um programa que leia a altura e a largura de uma parede em metros, 
#Calcule a sua área e a quantidade de tinta nescessária para pintá-la, 
#Sabendo que cada litro de tinta, pinta uma área de 2m².
alt = float(input('Digite a altura de sua parede: '))
larg = float(input('Digite a largura de sua parede: '))
área = alt * larg
print('A área total de sua parede é de {}m² e usará aproximadamente {}l de tinta'.format(área, área/2))
