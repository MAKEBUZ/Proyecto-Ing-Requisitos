class Usuario:
    def __init__(user, nombre_usuario, contrasenha, marca, numero, vencimiento, cvv):
        user.nombre_usuario = nombre_usuario
        user.contrasenha = contrasenha
        user.informacion_tarjeta_credito = {
            "marca": marca,
            "numero": numero,
            "vencimiento": vencimiento,
            "cvv": cvv
        }
        user.puntos = 0

    def modificar_informacion(user, nueva_contrasenha=None, nueva_marca=None, nuevo_numero=None, nuevo_vencimiento=None, nuevo_cvv=None):
        if nueva_contrasenha:
            user.contrasenha = nueva_contrasenha
        if nueva_marca or nuevo_numero or nuevo_vencimiento or nuevo_cvv:
            user.informacion_tarjeta_credito.update({
                "marca": nueva_marca or user.informacion_tarjeta_credito["marca"],
                "numero": nuevo_numero or user.informacion_tarjeta_credito["numero"],
                "vencimiento": nuevo_vencimiento or user.informacion_tarjeta_credito["vencimiento"],
                "cvv": nuevo_cvv or user.informacion_tarjeta_credito["cvv"]
            })

    def comprar_articulo(user, precio):
        if user.informacion_tarjeta_credito:
            user.puntos += precio // 10
            print("La canidad de puntos es: ", user.puntos)
            return True
        return False

    def canjear_puntos(user, puntos_requeridos):
        if user.puntos >= puntos_requeridos:
            user.puntos -= puntos_requeridos
            return True
        return False

class Producto:
    def __init__(user, nombre, precio):
        user.nombre = nombre
        user.precio = precio

class Premio:
    def __init__(user, nombre, puntos_requeridos):
        user.nombre = nombre
        user.puntos_requeridos = puntos_requeridos

usuarios = {}

def crear_usuario():
    nombre_usuario = input("Ingrese nombre de usuario: ")
    if nombre_usuario in usuarios:
        print("Nombre de usuario ya existe.")
        return
    
    contrasena = input("Ingrese una contraseña: ")
    marca = input("Ingrese la marca de la tarjeta: ")
    
    while True:
        tarjeta = input("Ingrese el número de tarjeta: ")
        n_tarjeta = len(tarjeta)
        
        if n_tarjeta != 16 or not tarjeta.isdigit():
            print("Error: Tarjeta no válida. Asegúrate de que tenga 16 dígitos numéricos.")
        else:
            break
    
    vencimiento = input("Ingrese la fecha de vencimiento: ")
    cvv = input("Ingrese el CVV: ")
    
    usuarios[nombre_usuario] = Usuario(nombre_usuario, contrasena, marca, tarjeta, vencimiento, cvv)
    print(f"Usuario '{nombre_usuario}' creado.")

def agregar_informacion_tarjeta(nombre_usuario, marca, numero, vencimiento, cvv):
    usuario = usuarios.get(nombre_usuario)
    if usuario:
        usuario.agregar_tarjeta_credito(marca, numero, vencimiento, cvv)
        print("Información de tarjeta agregada.")
    else:
        print("Usuario no encontrado.")

def comprar_articulo(nombre_usuario, precio):
    usuario = usuarios.get(nombre_usuario)
    if usuario:
        if usuario.comprar_articulo(precio):
            print("Compra exitosa.")
        else:
            print("Información de tarjeta faltante.")
    else:
        print("Usuario no encontrado.")

def canjear_puntos(nombre_usuario, puntos_requeridos):
    usuario = usuarios.get(nombre_usuario)
    if usuario:
        if usuario.canjear_puntos(puntos_requeridos):
            print("Puntos canjeados.")
        else:
            print("Puntos insuficientes.")
    else:
        print("Usuario no encontrado.")

productos = [
    Producto("GameYiar34", 150),
    Producto("Genshin Impact month pass", 3000),
    Producto("Canvas Pro", 50),
    Producto("Warzone",1900) 
]

premios = [
    Premio("Balón", 500),
    Premio("Juego de Mesa", 1300),
    Premio("Guantes", 200)
]

while True:
    print("\n1. Crear Cuenta")
    print("2. Comprar Artículo")
    print("3. Canjear Puntos por Premio")
    print("4. Modificar Información de la Cuenta")
    print("5. Ver Información de la Cuenta")
    print("6. Salir")
    
    eleccion = input("Seleccione una opción: ")
    
    if eleccion == "1":
        print("")
        crear_usuario()
        print("")
    elif eleccion == "2":
        print("")
        nombre_usuario = input("Ingrese nombre de usuario: ")
        print("Productos Disponibles:")
        for indice, producto in enumerate(productos, start=1):
            print(f"{indice}. {producto.nombre} - ${producto.precio}")
        eleccion_producto = int(input("Seleccione un producto para comprar: "))
        if 1 <= eleccion_producto <= len(productos):
            producto_seleccionado = productos[eleccion_producto - 1]
            comprar_articulo(nombre_usuario, producto_seleccionado.precio)
        else:
            print("Elección de producto inválida.")
        print("")
    elif eleccion == "3":
        print("")
        nombre_usuario = input("Ingrese nombre de usuario: ")
        print("Premios Disponibles:")
        for indice, premio in enumerate(premios, start=1):
            print(f"{indice}. {premio.nombre} - {premio.puntos_requeridos} puntos")
        eleccion_premio = int(input("Seleccione un premio para canjear: "))
        if 1 <= eleccion_premio <= len(premios):
            premio_seleccionado = premios[eleccion_premio - 1]
            canjear_puntos(nombre_usuario, premio_seleccionado.puntos_requeridos)
        else:
            print("Elección de premio inválida.")
        print("")
    elif eleccion == "4":
        print("")
        nombre_usuario = input("Ingrese nombre de usuario: ")
        usuario = usuarios.get(nombre_usuario)
        if usuario:
            print("Modificar Información de la Cuenta:")
            nueva_contrasenha = input("Nueva contraseña (dejar en blanco si no quieres cambiarla): ")
            nueva_marca = input("Nueva marca de la tarjeta (dejar en blanco si no quieres cambiarla): ")
            nuevo_numero = input("Nuevo número de tarjeta (dejar en blanco si no quieres cambiarlo): ")
            nuevo_vencimiento = input("Nuevo vencimiento de tarjeta (dejar en blanco si no quieres cambiarlo): ")
            nuevo_cvv = input("Nuevo CVV (dejar en blanco si no quieres cambiarlo): ")

            usuario.modificar_informacion(nueva_contrasenha, nueva_marca, nuevo_numero, nuevo_vencimiento, nuevo_cvv)
            print("Información de la cuenta modificada.")
        else:
            print("Usuario no encontrado.")
        print("")
    elif eleccion == "5":
        print("")
        nombre_usuario = input("Ingrese nombre de usuario: ")
        usuario = usuarios.get(nombre_usuario)
        if usuario:
            print("Información de la Cuenta:")
            print(f"Nombre de Usuario: {usuario.nombre_usuario}")
            print(f"Marca de Tarjeta: {usuario.informacion_tarjeta_credito['marca']}")
            print(f"Número de Tarjeta: {usuario.informacion_tarjeta_credito['numero']}")
            print(f"Fecha de Vencimiento: {usuario.informacion_tarjeta_credito['vencimiento']}")
            print(f"Puntos: {usuario.puntos}")
        else:
            print("Usuario no encontrado.")
        print("")
    elif eleccion == "6":
        print("")
        print("Saliendo del programa.")
        break
    else:
        print("")
        print("Opción inválida. Por favor seleccione una opción válida.")
        print("")
