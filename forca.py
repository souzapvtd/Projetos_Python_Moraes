def jogar_forca():
    print("------------------------------")
    print("Bem vindo ao Jogo da Forca")
    print("------------------------------")

    lista = ["_ _ _ _ _ _ "]

    palavra = "banana".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    perdeu = False
    acertou = False
    erros = 0
    #enquanto nao acerta a palavra secreta 
    #o jogador não pode jogar

    while (not perdeu and not acertou):
        chute = remover_acentos(input("Digite uma letra: ")).strip()
        #index define a posição da letra na palavra
        index = 0
    if(chute in palavra):
        for letra in palavra:
            if (chute.lower() == letra.lower()):
                letras_acertadas[index] = letra
            index = index + 1    
            
    else: 
        erros = erros + 1

        
    perdeu == 6
    acertou = "_" not in letras_acertadas






    print(letras_acertadas)


#como resolver ocento nas palavras

def remover_acentos(palavra):
    palavra = palavra.replace("á", "a")
    palavra = palavra.replace("é", "e")
    palavra = palavra.replace("í", "i")
    palavra = palavra.replace("ó", "o")
    palavra = palavra.replace("ú", "u")
    return palavra


if __name__ == "__main__":
    jogar_forca()
