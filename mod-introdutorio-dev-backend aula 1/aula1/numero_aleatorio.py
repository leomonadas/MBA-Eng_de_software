import random

# Escolha um número aleatório entre 1 e 5
# Receba um chute
# Se for igual ao número aleatório => Acertou
# Senão, quase, o número secreto era {numero_secreto}

# print(random.random())
# print(random.randint(2, 4))

print('Sejam bem-vindes ao jogo do número secreto!\n')

numero_secreto = random.randint(1,5)

numero_do_usuario = int(input('escolha um número entre 1 e 5: '))



if numero_secreto == numero_do_usuario:
    print(f'Parabéns! Você acertou o número secreto!')
else:
    print(f'Poxa, não foi dessa vez! Você achou que seria {numero_do_usuario} mas foi {numero_secreto}')