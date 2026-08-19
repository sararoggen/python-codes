# entrada

soma = 0
dados = []


N = int(input())

for i in range(N):
    carro = str(input()) #texto
    kml = float(input()) # valor
    dados.append((carro,kml))# adicionar o valor float na lista
    soma += kml # soma = soma + kmL
    
#saidas
media = soma/N
print(f"Consumo médio (km/l): {media:.1f}")

carro_mais_economico = dados[0] # atribui que a dupla1 seja o carro mais economico
for i in dados:
    if i[1] > carro_mais_economico[1]: # carro atual > carro da dupla e o valor do indice 1
        carro_mais_economico = i
print("Carro mais econômico:",carro_mais_economico[0]) #item 1 da dupla


print("Carros com taxa de consumo acima da média:")
acima_media = dados[0] 
for i in dados:
    if i[1] > media:# se for verdadeiro assume i = acima da media
        acima_media = i 
        print("-",i[0])
