def função2(dia,mes,ano):
    try:
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)
    except ValueError:
        return False
    
    if not 1<= mes <=12 and ano > 0: # se o mes exite de 1 a 12 e ano maior que zero
        return False
    
    if mes in [1,3,5,7,8,10,12]: #meses com 31 dias
        max_dias = 31
    elif mes in [4,6,9,11]: #meses com 30 dias
        max_dias = 30
    elif mes == 2: # mes de fev, 28 dias
        max_dias = 28
    else:
        return False
    
    return 1 <= dia <= max_dias
         

def função1(data):
    valores = data.split("/")
    DD = valores[0]
    MM = valores[1]
    AAAA = valores[2]
    
    meses = {"01":"Janeiro","02":"Fevereiro","03":"Março",
             "04":"Abril","05":"Maio","06":"Junho","07":"Julho","08":"Agosto",
             "09":"Setembro","10":"Outubro","11":"Novembro","12":"Dezembro"}
    nome_do_mes = meses.get(MM)
    validação = função2(DD,MM,AAAA)
    
    if validação == True:
        print(DD,"de",nome_do_mes,"de",AAAA)
    else:
        print("Data inválida")

    
#programa principal
data = input()
função1(data)
