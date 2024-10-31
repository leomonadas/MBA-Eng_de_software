print('Calcule seu IMC\n')

#Peso / Altura ^2
peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
imc = peso / altura**2
imc = round(imc, 2)

print(f'\nO seu IMC é {imc}.')