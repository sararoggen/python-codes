# entrada
candidato1 = str(input(""))
candidato2 = str(input(""))
candidato3 = str(input(""))

#exceções
try:
    int1 = int(input(""))
    int2 = int(input(""))
    int3 = int(input(""))
except:
    print("Entrada inválida")

#condição numeros positivos
if int1 <=0 or int2 <=0 or int3 <=0: 
    print("Entrada inválida")

# variaveis para calculo porcentagem
total = int1 + int2 + int3
calculo1 = (100*int1)/(total)
calculo2 = (100*int2)/(total)
calculo3 = (100*int3)/(total)

      
# condições
if total >= 20000: #primeiro turno
    if calculo1 > 50:
        print(candidato1,"venceu no primeiro turno com", calculo1, "dos votos")
    elif calculo2 > 50:
        print(candidato2,"venceu no primeiro turno com", calculo2, "dos votos")
    elif calculo3 > 50:
        print(candidato3,"venceu no primeiro turno com", calculo3, "dos votos")
    else:
         #segundo turno #saida da variavel
        if calculo1 < 50 and calculo2 < 50:
            print(candidato1, "e", candidato2, "disputarão o segundo turno com", f"{calculo1:.2f}", "% e", f"{calculo2:.2f}", "% votos respectivamente")
        elif calculo2 < 50 and calculo3 < 50:
            print(candidato2, "e", candidato3, "disputarão o segundo turno com", f"{calculo2:.2f}", "% e", f"{calculo3:.2f}", "% votos respectivamente")
        elif calculo3 < 50 and calculo1 < 50:
            print(f"{calculo3:.2f}", "e", f"{calculo1:.2f}", "disputarão o segundo turno com", f"{calculo3:.2f}", "% e", f"{calculo3:.2f}", "% votos respectivamente")
        elif calculo2 < 50 and calculo1 < 50:
            print(candidato2, "e", candidato1, "disputarão o segundo turno com", f"{calculo2:.2f}", "% e", f"{calculo3:.2f}", "% votos respectivamente")
        elif calculo3 < 50 and calculo2 < 50:
            print(candidato3, "e", candidato2, "disputarão o segundo turno com", f"{calculo3:.2f}", "% e", f"{calculo2:.2f}", "% votos respectivamente")
        else:
            print(candidato1, "e", candidato3, "disputarão o segundo turno com", f"{calculo1:.2f}", "% e", f"{calculo3:.2f}", "% votos respectivamente")
        
        
        
    
