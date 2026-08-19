# entrada
l1 = float(input(""))
l2 = float(input(""))
l3 = float(input(""))

#condições

if (l1 > (l2 + l3)) or (l2 > (l1 + l3)) or (l3 > (l1 + l2)) or l1 == 0 or l2 == 0 or l3 == 0:
    print("triangulo invalido")
elif l1 == l2 == l3:
    print("triangulo equilátero")
elif l1 == l2 or l2 == l3 or l3 == l1:
    print("triangulo isosceles")
else:
    print("triangulo escaleno")

