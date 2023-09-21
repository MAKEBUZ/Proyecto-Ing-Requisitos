clientes = []
coches = []
reservas = []


def agregar_cliente():
    codigo = input("Ingrese el código del cliente: ")
    dni = input("Ingrese el DNI del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    
  
    avalado_por = input("¿Este cliente está avalado por otro cliente? (S/N): ")
    if avalado_por.upper() == "S":
        codigo_avalador = input("Ingrese el código del cliente avalador: ")
        cliente_avalador = buscar_cliente_por_codigo(codigo_avalador)
        if cliente_avalador:
            cliente_avalador["avalados"].append(codigo)
    
    clientes.append({
        "Codigo": codigo,
        "DNI": dni,
        "Nombre": nombre,
        "Direccion": direccion,
        "Telefono": telefono,
        "Avalados": []
    })


def buscar_cliente_por_codigo(codigo):
    for cliente in clientes:
        if cliente["codigo"] == codigo:
            return cliente
    return None


def agregar_coche():
    matricula = input("Ingrese la matrícula del coche: ")
    modelo = input("Ingrese el modelo del coche: ")
    color = input("Ingrese el color del coche: ")
    marca = input("Ingrese la marca del coche: ")
    garaje = input("Ingrese el garaje asignado del coche: ")
    
    coches.append({
        "Matricula": matricula,
        "Modelo": modelo,
        "Color": color,
        "Marca": marca,
        "Garaje": garaje
    })

def buscar_coche_por_matricula(matricula):
    for coche in coches:
        if coche["matricula"] == matricula:
            return coche
    return None

def agregar_reserva():
    codigo_cliente = input("Ingrese el código del cliente que realiza la reserva: ")
    cod_cliente = buscar_cliente_por_codigo(codigo_cliente)
    
    if cod_cliente in clientes:
        for i in range(len(coches)):
            print(coches[i], end= '\n')
    elif cod_cliente is None:
        print("Cliente no encontrado.")
        return
    
    fecha_inicio = input("Ingrese la fecha de inicio de la reserva (AAAA-MM-DD): ")
    fecha_fin = input("Ingrese la fecha de fin de la reserva (AAAA-MM-DD): ")
    agencia = input("Ingrese el nombre de la agencia de reserva: ")
    
    reserva = {
        "cliente": cod_cliente,
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin,
        "agencia": agencia,
        "coches": [],
        "precio_total": 0,
        "litros_gasolina": 0,
        "entregado": False
    }

    while True:
        matricula_coche = input("Ingrese la matrícula del coche a reservar (o '0' para finalizar): ")
        if matricula_coche == '0':
            break
        
        coche = buscar_coche_por_matricula(matricula_coche)
        if coche is None:
            print("Coche no encontrado.")
            continue
        
        precio_alquiler = float(input(f"Ingrese el precio de alquiler para el coche {matricula_coche}: "))
        
        reserva["coches"].append({
            "coche": coche,
            "precio_alquiler": precio_alquiler
        })
    
    reservas.append(reserva)

def calcular_precio_total(reserva):
    reserva["precio_total"] = sum(item["precio_alquiler"] for item in reserva["coches"])


def entregar_coches():
    codigo_reserva = input("Ingrese el código de la reserva a entregar: ")
    reserva = buscar_reserva_por_codigo(codigo_reserva)
    
    if reserva is None:
        print("Reserva no encontrada.")
        return
    
    litros_gasolina = float(input("Ingrese la cantidad de litros de gasolina al entregar los coches: "))
    reserva["litros_gasolina"] = litros_gasolina
    reserva["entregado"] = True


def buscar_reserva_por_codigo(codigo):
    for reserva in reservas:
        if reserva["cliente"]["codigo"] == codigo:
            return reserva
    return None

def buscar_cliente():
    buscar_cliente = input("Ingrese el código del cliente que desea consultar: ")
    srch_cliente = buscar_cliente_por_codigo(buscar_cliente)

    if srch_cliente in clientes:
        for i in range(len(clientes)):
            print(clientes[i], end= '\n')
    elif srch_cliente is None:
        print("Cliente no encontrado.")
        return



while True:
    print("\nMenú Principal:")
    print("1. Agregar Cliente")
    print("2. Agregar Coche")
    print("3. Realizar Reserva")
    print("4. Entregar Coches de Reserva")
    print("5. Consultar Clientes")
    print("6. Salir")
    
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        agregar_cliente()
    elif opcion == "2":
        agregar_coche()
    elif opcion == "3":
        agregar_reserva()
    elif opcion == "4":
        entregar_coches()
    elif opcion == "5":
        buscar_cliente()
    elif opcion == "6":
        break
    else:
        print("Opción no válida. Intente nuevamente.")
