# inicio abertura do jogo
print("============")
print("Cifra de César")
print("============")
print()
print("A Cifra de César é um método de criptografia")
print("de substituição simples onde cada letra de uma")
print("mensagem é substituída pela letra que se encontra")
print("um número fixo de posições à frente no alfabeto")
print()
print("Você terá 10 créditos para tentar decifrar a chave")
print("de deslocamento da mensagem cifrada.")
print()
print("Boa sorte!")
print()
print("Pressione ENTER")
input()

# implentação sorteio de frases
import random

frases_disponiveis = [
    "VOCE E MUITO LABUBONICA",
    "MORANGO DO AMOR E MUITO BOM",
    "VOU IR NA FESTA DO CARLINHOS MAIA",
    "A VIRGINIA E MINHA IDOLA",
    "ADORO PINTAR BOBBIE GOODS",
    "GOSTO DE SORVETE DE PISTACHE",
    "COMPREI UM LABUBU" ]

frase_sorteada = random.choice(frases_disponiveis)
# a frase "sorteada"

chave_sorteada = random.randint(1, 26)

#chave "sorteada"

#criptografia

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#define o alfabeto como string

frase_criptografada = ""
tamanho_alfabeto = len(alfabeto)

for caractere in frase_sorteada:
    if caractere in alfabeto: #se o caractere for uma letra
        posiçao_inicial = alfabeto.index(caractere) #encontrar o indice da caractere
        posiçao_nova = (posiçao_inicial + chave_sorteada)% tamanho_alfabeto #criptografia
        caractere_criptografado = alfabeto[posiçao_nova] #volta a ser letra
        frase_criptografada += caractere_criptografado
    else:
        frase_criptografada += caractere #para espaços continuarem sendo espaços
tamanho_frase = len(frase_criptografada)
print("="*tamanho_frase)
print(frase_criptografada)
print("="*tamanho_frase)
print()
print(1,". Adivinhar a chave",sep = "")
print(2,". Solicitar dicas",sep = "")

print("Selecione uma opção:")
opçao = -1
while opçao != 0:
    opçao = int(input())
    if opçao == 1:
        print("#########")
        print("TENTATIVA")
        print("#########")
        print("Digite um valor para a chave:")
        tentativa = int(input())

        if tentativa != chave_sorteada:
            frase_criptografada2 = ""
            tamanho_alfabeto2 = len(alfabeto)
            frase_sorteada2 = frase_sorteada

            for caractere2 in frase_sorteada2:
                if caractere2 in alfabeto: #se o caractere for uma letra
                    posiçao_inicial2 = alfabeto.index(caractere2) #encontrar o indice da caractere
                    posiçao_nova2 = (posiçao_inicial2 + tentativa)% tamanho_alfabeto2 #criptografia
                    caractere_criptografado2 = alfabeto[posiçao_nova2] #volta a ser letra
                    frase_criptografada2 += caractere_criptografado2
                else:
                    frase_criptografada2 += caractere2 #para espaços continuarem sendo espaços
            tamanho_frase2 = len(frase_criptografada2)
            print("="*tamanho_frase2)
            print(frase_criptografada2)
            print("="*tamanho_frase2)
            
    elif opçao == 2:
        print("dica")

    
