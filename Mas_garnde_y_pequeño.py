n1 = int(input("Ingresa el numero 1\n"))
n2 = int(input("Ingresa el numero 2\n"))
n3 = int(input("Ingresa el numero 3\n"))
n4 = int(input("Ingresa el numero 4\n"))
nmayor = 0
nmenor = 999999999999999999999999999999999

if n1>nmayor:
    nmayor = n1

if n2>nmayor:
    nmayor = n2

if n3>nmayor:
    nmayor = n3

if n4>nmayor:
    nmayor = n4

print("El numero menor es: ",nmayor)

if n1<nmenor:
    nmenor = n1

if n2<nmenor:
    nmenor = n2

if n3<nmenor:
    nmenor = n3

if n4<nmenor:
    nmenor = n4

print("El numero menor es: ",nmenor)