ingreso_c = float(input("¿De cuanto es tu ingreso?"))

if ingreso_c<85528:
    impuesto = ingreso_c*.18-556.02
else:
    impuesto = (ingreso_c + 85528)*.32+1483.02
    
if impuesto < 0.0:
    impuesto = 0.0
impuesto = round(impuesto,0)
print("El impuesto es: ",impuesto," pesos")
    