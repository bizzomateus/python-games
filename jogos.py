import forca
import adivinha

if __name__ == "__main__":
    
    print(30*'#')
    print('##### Escolha seu jogo. #####')
    print(30*'#')
    
    print('\n (1)Forca (2)Adivinhação: ')
    jogo = input('Escolha: ')

    if (jogo == '1'):
        forca.jogar()
    elif (jogo == '2'):
        adivinha.jogar()
    else:
        print('Escolha inválida')
        