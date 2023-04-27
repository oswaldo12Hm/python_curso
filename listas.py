# #Listas
# numeros=[10,5,9,6,3,7,4,2]
# #maneras de insertar
# numeros.append(99)
# numeros.insert(0,88)
# print(numeros)

# print(numeros[1])

# numeros[5]=111
# print(numeros)

# numeros[0]=numeros[5]
# print(numeros)

# numeros[2]=numeros[1]+numeros[4]
# print(numeros)
# print(len(numeros))

# del numeros[1]
# print(numeros)
# print(len(numeros))
# #----------------------------------------------------
# mi_lista=[]
# for i in range(5):
#     mi_lista.append(i+1)
# print(mi_lista)
# #------------------------------------------------------
# mi_lista2=[]
# for i in range(5):
#     mi_lista2.insert(0, i+1)
# print(mi_lista2)

# total=0
# for i in range(len(mi_lista2)):
#     total+=mi_lista2[1]
# print(total)
# #-----------------------
# Lista=[1,5,9,8,6]
# Lista[0],Lista[4],Lista[3],Lista[1]=Lista[4],Lista[0],Lista[1],Lista[3]
# print(Lista)
#-----------------------------------------------------
# Lista2=[1,5,15,90,64,24,9,8,6,8,78,36]
# for i in range(len(Lista2)//2):
#     Lista2[i],Lista2[len(Lista2)-i-1]=Lista2[len(Lista2)-i-1],Lista2[i]
# print(Lista2)
#----------------------------------------------------------------------------
# print("Ejercicio Bronco")
# bronco=["LUPE","JOSE LUIS","CHOCHE","RAMIRO"]
# print(bronco)
# bronco.append("PELON")
# print(bronco)
# del bronco[1]
# del bronco[1]
# del bronco[1]
# del bronco[1]
# print(bronco)
# bronco.append("RAMIRO")
# print(bronco)
# bronco.append("HUGO")
# bronco.append("PACO")
# bronco.append("LUIS")
# print(bronco)
#------------------------------------------------
# listass=[1,None,True,"Cadena",256,5.3,[1,2,3]]
# print(listass)
#------------------------------------------------
# Nlis=["blanco","azul","amarillo","verde","morado"]
# print(Nlis)
# for color in Nlis:
#     print(color)
#----------------------------------------------------
# desorden=[5,7,6,8,9,2,1]
# print(desorden)
# desorden.sort()
# print(desorden)
# #---------------------------------------------------
# lst=["A","Z","G","T"]
# print(lst)
# lst.sort()
# print(lst)
# lst.reverse()
# print(lst)
# #----------------------------------------------------------
# lis_1=[1]
# lis_2=lis_1
# lis_1[0]=2
# print(lis_2)
#----------------------------------------------------
# lis_1=[1]
# lis_2=lis_1[:]
# lis_1[0]=2
# print(lis_1)
# print(lis_2)
#----------------------------------------------------------
# lis_1=[1,2,6,54,5,7,9,10,47,60]
# lis_2=lis_1[2:6]
# lis_1[0]=2
# print(lis_1)
# print(lis_2)
# print(5 in lis_1)
# print(5 not in lis_2)
#---------------------------------------------------------
arena=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
buscra=10
for i in range(len(arena)):
    encontrar=arena[i]==buscra
    if encontrar:
        break
if encontrar:
    print("ENCONTRADO EN: ",i)
else:
    print("NO ENCONTRADO")