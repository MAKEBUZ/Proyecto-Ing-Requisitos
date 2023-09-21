# Definir listas para almacenar la información
empresas = []
empleados = []
clientes = []

def crear_empresa():
    nombre_empresa = input("Nombre de la empresa: ")
    empresas.append(nombre_empresa)
    print(f"Empresa '{nombre_empresa}' creada con éxito.")

def agregar_empleado():
    if not empresas:
        print("No hay empresas creadas. Crea una empresa primero.")
        return

    print("Empresas disponibles:")
    for i, empresa in enumerate(empresas):
        print(f"{i + 1}. {empresa}")

    empresa_code = int(input("Selecciona el número de empresa al que deseas agregar el empleado: ")) - 1

    nombre = input("Nombre del empleado: ")
    edad = int(input("Edad del empleado: "))
    sueldo_bruto = float(input("Sueldo Bruto del empleado: "))
    es_directivo = input("¿Es un directivo? (Sí/No): ").lower() == "si"
    categoria = None
    subordinados = 0
    if es_directivo:
        categoria = input("Categoría del directivo: ")
        subordinados = int(input("Número de subordinados: "))
    empleado = {
        "Nombre": nombre,
        "Edad": edad,
        "Sueldo Bruto": sueldo_bruto,
        "Es Directivo": es_directivo,
        "Categoría": categoria,
        "Subordinados": subordinados
    }
    empleados.append((empresas[empresa_code], empleado))
    print("Empleado agregado con éxito.")

def agregar_cliente():
    if not empresas:
        print("No hay empresas creadas. Crea una empresa primero.")
        return

    print("Empresas disponibles:")
    for i, empresa in enumerate(empresas):
        print(f"{i + 1}. {empresa}")

    empresa_code = int(input("Selecciona el número de empresa a la que deseas agregar el cliente: ")) - 1

    nombre = input("Nombre del cliente: ")
    edad = int(input("Edad del cliente: "))
    telefono = input("Teléfono del cliente: ")
    cliente = {
        "Nombre": nombre,
        "Edad": edad,
        "Teléfono": telefono
    }
    clientes.append((empresas[empresa_code], cliente))
    print("Cliente agregado con éxito.")

def mostrar_empleados():
    if not empresas:
        print("No hay empresas creadas. Crea una empresa primero.")
        return

    print("Empresas disponibles:")
    for i, empresa in enumerate(empresas):
        print(f"{i + 1}. {empresa}")

    empresa_code = int(input("Selecciona el número de empresa cuyos empleados deseas mostrar: ")) - 1
    empresa = empresas[empresa_code]
    print(f"Empleados de {empresa}:")
    for e in empleados:
        if e[0] == empresa:
            empleado = e[1]
            print(f"Nombre: {empleado['Nombre']}, Edad: {empleado['Edad']}, Sueldo Bruto: {empleado['Sueldo Bruto']}")
            if empleado['Es Directivo']:
                print(f"Categoría: {empleado['Categoría']}, Subordinados: {empleado['Subordinados']}")

def mostrar_clientes():
    if not empresas:
        print("No hay empresas creadas. Crea una empresa primero.")
        return

    print("Empresas disponibles:")
    for i, empresa in enumerate(empresas):
        print(f"{i + 1}. {empresa}")

    empresa_code = int(input("Selecciona el número de empresa cuyos clientes deseas mostrar: ")) - 1
    empresa = empresas[empresa_code]
    print(f"Clientes de {empresa}:")
    for c in clientes:
        if c[0] == empresa:
            cliente = c[1]
            print(f"Nombre: {cliente['Nombre']}, Edad: {cliente['Edad']}, Teléfono: {cliente['Teléfono']}")

while True:
    print("\nMenu:")
    print("1. Crear empresa")
    print("2. Agregar empleado a empresa")
    print("3. Agregar cliente a empresa")
    print("4. Mostrar empleados de empresa")
    print("5. Mostrar clientes de empresa")
    print("6. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        crear_empresa()
    elif opcion == "2":
        agregar_empleado()
    elif opcion == "3":
        agregar_cliente()
    elif opcion == "4":
        mostrar_empleados()
    elif opcion == "5":
        mostrar_clientes()
    elif opcion == "6":
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")