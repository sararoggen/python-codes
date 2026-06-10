# usuario vai colocar os números certos, não preciso colocar try/except

#inicio: nenhum item for selecionado
suco = 0
refri = 0
hamburguer_duplo = 0
hamburguer_simples = 0
fritas = 0

#laço
produto = 1 #valor diferente de zero para ser verdadeiro
while produto >  0:
    produto = int(input())
    if produto == 1:
        suco += 1
    elif produto == 2:
        refri += 1
    elif produto == 3:
        hamburguer_simples += 1
    elif produto == 4:
        hamburguer_duplo += 1
    elif produto == 5:
        fritas += 1
        
#variaveis de saídas
bebidas = suco + refri
total = suco*5.00 + refri*8.50 + hamburguer_simples*25.80 + hamburguer_duplo*28.40 + fritas*15.00
lucro = total*0.30

#saída
print("- Relatório da Venda -")
print("Quantidade de bebidas vendidas:",bebidas)
print(f"Valor total: R$ {total:.2f}")
print(f"Lucro obtido: R$ {lucro:.2f}")

if fritas > 0:
    print("Batatas fritas vendidas? Sim")
else:
    print("Batatas fritas vendidas? Não")
    
#hamburguer mais vendido
if hamburguer_simples > hamburguer_duplo:
    print("Hambúrguer mais vendido: Simples")
elif hamburguer_duplo > hamburguer_simples:
    print("Hambúrguer mais vendido: Duplo")
elif hamburguer_duplo == hamburguer_simples and hamburguer_duplo != 0 and hamburguer_simples != 0:
    print("Hambúrguer mais vendido: Empate")
elif hamburguer_simples == 0 or hamburguer_duplo == 0 :
    print("Hambúrguer mais vendido: Nenhum")
