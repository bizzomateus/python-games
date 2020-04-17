import random

def jogar():
    
    print(45*"#")
    print("##### Bem-vindo ao jogo Forca. #####")
    print(45*"#")

    palavras = []
    with open("palavras.txt", "r") as arquivo:
        for palavra in arquivo:
            palavras.append(palavra.strip())

    randindex = random.randrange(0, len(palavras))

    palavra_secreta = palavras[randindex].lower()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
        
    while (not acertou and not enforcou):
        chute = input("Tente uma letra: ")
        chute = chute.strip().lower()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra

                index += 1
        else:
            erros += 1
            if "_" in letras_acertadas and not erros == len(palavra_secreta):
                faltantes = len(palavra_secreta)-erros
                print(f"Você errou e ainda tem {faltantes} vidas.")

        enforcou = erros == len(palavra_secreta)
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print("Você ganhou!")
    else:
        print("Você perdeu!")
    print("Fim de Jogo")

if __name__ == "__main__":
    jogar()
    