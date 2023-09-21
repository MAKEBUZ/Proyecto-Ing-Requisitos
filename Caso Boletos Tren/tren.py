#Elaborado por Diego Ocampo

def digitos(numero):
    return str(numero)[-4:]

print("Programa para generar un boleto de tren")

while True:
    print("Se encuentra en la estación Wiskonsin")
    print("Seleccione su destino:")
    print("1. Niuv York (Valor: $150,000)")
    print("2. Yourichi (Valor: $50,000)")
    print("3. Melgar (Valor: $200,000)")
    print("4. Fostrap (Valor: $130,000)")
    num_estacion = int(input("Ingrese el número de la estación de destino: "))

    if num_estacion in [1, 2, 3, 4]:
        if num_estacion == 1:
            valor_boleto = 150000
        elif num_estacion == 2:
            valor_boleto = 50000
        elif num_estacion == 3:
            valor_boleto = 200000
        else:
            valor_boleto = 130000

        print(f"El valor del boleto es: ${valor_boleto} COP")
        id = input("Ingrese su número de Identificación: ")
        tarjeta = input("Ingrese su número de tarjeta (sin espacios): ")
        n_tarjeta = len(tarjeta)
        n_id = len(id)

        if n_tarjeta !=16 or not tarjeta.isdigit():
            print("Error --- Tarjeta no válida")
            break
        if n_id != 10 or not id.isdigit():
            print("Error --- Identificación no válida")
            break

        print(f"El valor total del boleto es: ${valor_boleto}")
        print(f"Su número de identificación es: {id}")
        print(f"El cobro se efectuará a la tarjeta terminada en: {digitos(tarjeta)}")
    else:
        print("Destino no válido. Inténtelo de nuevo.")
    break
