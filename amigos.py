# entrada
N1 = int(input())
N2 = int(input())
soma1 = 0
soma2 = 0

# laço para N1
print("Divisores próprios de",N1,end = "")
print(":",end = " ")

for i in range(1,N1):
    if N1 % i == 0:
        soma1 += i
        print(i,end = " ")
print("cuja soma é",soma1)


# laço para N2
print("Divisores próprios de",N2,end = "")
print(":",end = " ")

for i in range(1,N2):
    if N2 % i == 0:
        soma2 += i
        print(i,end = " ")
print("cuja soma é",soma2)

if soma1 == N2 and soma2 == N1: #são amigos
    print(N1,"e",N2,"são amigos")
else: # não são amigos
    print(N1,"e",N2,"não são amigos")
