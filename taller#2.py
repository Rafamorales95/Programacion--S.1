tarifa = 0
cantidad = int(input("Ingrese cantidad de minutos: "))

print("\n1. Estados Unidos")
print("2. Canadá")
print("3. Europa")
print("4. Resto del mundo")
destino = int(input("Seleccione destino: "))

if destino >= 1 and destino <= 4:
    if destino == 1:  # estados unidos
        tarifa = 900
    elif destino == 2:  # canada
        tarifa = 800
    elif destino == 3:  # europa
        tarifa = 950
    else:  # resto del mundo
        tarifa = 1250

    costo_total = tarifa * cantidad
    descuento = 0
    if cantidad > 15:  # aplicar descuento de 20%
        descuento = costo_total * 0.20

    costo_total = costo_total - descuento
    print(f"El costo de llamada total es de: {costo_total}")
else:
    print("El destino seleccionado es incorrecto")