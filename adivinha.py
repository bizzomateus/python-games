import random

NUMBER = random.randrange(1,101)
total_tentativas = 0
pontos = 1000

def jogar():
    print(45*'#')
    print('##### Bem-vindo ao jogo de Adivinhação. #####')
    print(45*'#')

    while (total_tentativas == 0):
        print('\n(1)Fácil (2)Médio (3)Difícil')
        nivel = int(input('Escolha um nível: '))

        if (nivel == 1):
            print("Nível fácil. Você terá 20 chances.")
            total_tentativas = 20
        elif (nivel == 2):
            print('Nível médio. Você terá 10 chances.')
            total_tentativas = 10
        elif (nivel == 3):
            print('Nível difícil. Você terá 5 chances.')
            total_tentativas = 5
        else:
            print('Digite o número referente ao nível.')
            continue

    for rodada in range(1, total_tentativas+1):
        print(f'\nTentativa {rodada} de {total_tentativas}')
        chute = int(input('Digite um número: '))

        if (chute < 1) or (chute > 100):
            print('O numero está entre 0 e 100.')
            continue

        acerto = (chute == NUMBER)
        maior = (chute > NUMBER)

        if acerto:
            print(f'Parabéns, você ganhou! Score: {pontos}')
            break
        elif (rodada == total_tentativas):
            print(f'Errado. O número secreto era {NUMBER}. Você fez {pontos}')
            break
        elif maior:
            print('Errado. Tente um numero menor.')
        else:
            print('Errado. Tente um numero maior.')

        pontos_perdidos = abs(NUMBER - chute)
        pontos = pontos - pontos_perdidos

    print('Game Over')

if __name__ == "__main__":
    jogar()
