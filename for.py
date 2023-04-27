i=0
# for i in range(10):
#     print(i+1)
#-------------------------------------------
# for i in range(2,8):
#     print("El valor de i es: ",i)
#------------------------------------------
# for i in range(2,8,3):
#     print("El valor de i es: ",i)
#-------------------------------------------
# for i in range(1,1):
#     print("El valor de i es: ",i)
#-------------------------------------------
# base=1
# for i in range(16):
#     print("2 a la potencia de ",i," es: ",base)
#     base*=2
#--------------------------------------------
# from time import sleep
# numeros = range(1,6)
# for numeros in numeros:
#       print(f'{numeros} mississipi')
#       sleep(1)
# print("Listos ya voy")
#---------------------------------------------
# numeros = range(1,11)
# for numeros in numeros:
#     if numeros%5==0:
#         break
#     print(f"Dentro del bucle")
# print("Fueta del bucle")
#----------------------------------------------
# numeros = range(1,11)
# for numeros in numeros:
#     if numeros%5==0:
#         continue
#     print(f"Dentro del bucle")
# print("Fueta del bucle")
#---------------------------------------------
# vocales=['A','E','I','O','U']
# palabra = input("Ingresa una palabra\n").upper()
# for letra in palabra:
#     if not letra in vocales:
#         print(letra,end=" ")
#----------------------------------------------------
# vocales=['A','E','I','O','U']
# nueva_palabra=""
# palabra = input("Ingresa una palabra\n").upper()
# for letra in palabra:
#     if not letra in vocales:
#         nueva_palabra += letra
# print(nueva_palabra)
#-------------------------------------------------------
# for i in range(5):
#     print(i)
# else:
#     print("else: ",i)
#-------------------------------------------------------
# i=111
# for i in range(2,1):
#     print(i)
# else:
#     print("else: ",i)
#------------------------------------------------------
# word = "PYTHON"
# for letter in word:
#     print(letter,end="*")
#------------------------------------------------------
numeros=['0','1','2','3','4','5','6','7','8','9']
nueva_palabra=""
correo=input("Ingresa tu correo\n")
for num in correo:
    if  num in numeros:
        nueva_palabra += num
print(nueva_palabra)
