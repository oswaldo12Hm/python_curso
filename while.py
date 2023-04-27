# # while True:
# #     print("Estoy en un ciclo infinito")
# #-------------------------------------------------------
# respuesta = 1
# sum = 0
# while respuesta != 0:
#     respuesta = int(input("Escribe 0 para salir\n"))
#     sum = sum + 1
#     print(sum)
#-----------------------------------------------------------
# import random
# numero_secreto=random.randint(0,999)
# print("Este es mi juego y tienes que adivinar para salir")
# print("¿Que numero estoy pensando?")
# while True:
#     numero_usuario = int(input("Ingresa el numero\n"))
#     if numero_usuario < numero_secreto:
#         print("Es mas grande")
#     elif numero_usuario > numero_secreto:
#         print("Es mas pequeño")
#     else:
#         break
# print("LO ADIVINASTE")
#---------------------------------------------------------------
# i=1
# while i<5:
#     print(i)
#     i+=1
# else:
#     print("else: ",i)
my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list[2][0])