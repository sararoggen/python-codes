#INICIO, variaveis = 0, na lista
X = 0
Y = ""
Z = 0
W = 0.0

J = 0.0
prodouto = [] # lista de cada z*w

# laço de entrada até o usuário digitar 2 ou 3
requisição = -1 # INPUT ,numero q aparece antes do produto
while requisição != 0:
    requisição = int(input())

    if  requisição == 1:
        produto = input()
        l = produto.split(", ") #cria lista com cada termo de produto
        X = int(l[0]) #codigo
        Y = str(l[1]) #nome
        Z = int(l[2]) #quantidade 
        W = float(l[3]) #valor
        
    elif requisição == 2: #venda
        X, Z = input().split(", ")
        
        for l in produto:
            if l[0] == X:
                if l[2] < Z:
                    print("Quantidade insuficiente")
                else:
                    K = Z*l[3]
                    J += valor_compra
                    l[2] -= Z
                    if l[2] == 0:
                        X,Z.remove(l)
                break
            else:
                print("Produto inválido")
                        
    elif requisição == 3: #exibir
        for l in produto:
            print("ID:",X,"NOME:",Y,"QUANTIDADE:",Z,"VALOR: R$",W)
    else:
        print(f"VALOR DA COMPRA: R${K:.2f}")
        print(f"TOTAL VENDIDO: R${J:.2f}")


        #cadastro.append((((ID, nome, quantidade, valor))))


