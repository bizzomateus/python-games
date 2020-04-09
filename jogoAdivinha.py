import random
NUMBER = random.randrange(1,101)

print(30*'#')
print('Vamos começar o jogo de adivinhação.')
print(30*'#')
rodadas = input('\nQuantas rodadas você quer jogar?\n')
total_tentativas = int(rodadas)

for rodada in range(1, total_tentativas+1):
    print(f'Tentativa {rodada} de {total_tentativas}')
    chute = int(input('Digite um número: '))

    if (chute <= 1) or (chute >= 100):
        print('O numero está entre 0 e 100.')
        continue

    acerto = (chute == NUMBER)
    maior = (chute > NUMBER)

    if acerto:
        print('Parabens, você ganhou!')
        break
    elif maior:
        print('Errado. Tente um numero menor.')
    else:
        print('Errado. Tente um numero maior.')

print('Game Over')
