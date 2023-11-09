from Builders.masa_builder import MasaPizzaBuilder
from Builders.salsa_builder import SalsaPizzaBuilder
from Builders.coccion_builder import CoccionPizzaBuilder
from Builders.presentacion_builder import PresentacionPizzaBuilder
from Builders.ingredientes_builder import IngredientesPizzaBuilder
from Builders.extras_builder import ExtrasPizzaBuilder
from Builders.maridajes_builder import BebidaPizza
from storage.csv_handler import CSVHandler
from cliente import Cliente

# Función para el registro de usuario
def registrar_usuario(csv_handler):
    usuario_nuevo = {}
    nombre_usuario = input("Introduce tu nombre de usuario: ")
    contraseña = input("Introduce tu contraseña: ")

    usuario_nuevo['Nombre'] = nombre_usuario
    usuario_nuevo['Contraseña'] = contraseña

    # Agregar el nuevo usuario al archivo CSV
    csv_handler.guardar_usuario(usuario_nuevo)
    print("Usuario registrado con éxito.")

if __name__ == "__main__":
    # Instancia de builders para construir la pizza
    masa_builder = MasaPizzaBuilder()
    salsa_builder = SalsaPizzaBuilder()
    coccion_builder = CoccionPizzaBuilder()
    presentacion_builder = PresentacionPizzaBuilder()
    ingredientes_builder = IngredientesPizzaBuilder()
    extras_builder = ExtrasPizzaBuilder()
    maridaje_builder = BebidaPizza()

    # Manejador CSV para usuarios
    csv_handler_usuarios = CSVHandler('usuarios.csv')

    # Registro de usuario
    registrar_usuario(csv_handler_usuarios)

    # Iniciar sesión
    cliente = Cliente()

    usuario_valido = False
    while not usuario_valido:
        usuario = input("Nombre de usuario: ")
        contraseña = input("Contraseña: ")

        usuario_valido = cliente.iniciar_sesion(csv_handler_usuarios, usuario, contraseña)

        if usuario_valido:
            print("Inicio de sesión exitoso.")
        else:
            print("Nombre de usuario o contraseña incorrectos.")

    # Interacción para construir la pizza
    masa = cliente.elegir_masa(masa_builder)
    salsa = cliente.elegir_salsa(salsa_builder)
    coccion = cliente.elegir_coccion(coccion_builder)
    presentacion = cliente.elegir_presentacion(presentacion_builder)
    ingredientes = cliente.elegir_ingredientes(ingredientes_builder)
    extras = cliente.elegir_extras(extras_builder)
    maridaje = cliente.elegir_maridaje(maridaje_builder)

    from usuario import registrar_usuario, autenticar_usuario

# Función para realizar un pedido
def hacer_pedido(nombre_usuario):
    # Aquí realizarías el pedido
    pedido = {
        'usuario': nombre_usuario,
        'detalles': '...detalles del pedido...',
        # Otros detalles del pedido
    }
    return pedido

if __name__ == "__main__":
    # Pedir al usuario que se registre o inicie sesión
    nombre_usuario = input("Introduce tu nombre de usuario: ")
    contraseña = input("Introduce tu contraseña: ")

    if not autenticar_usuario(nombre_usuario, contraseña):
        registrar_usuario(nombre_usuario, contraseña)
        print("Te has registrado con éxito. Ahora puedes realizar tu pedido.")
    else:
        print("¡Bienvenido de nuevo!")

    # Realizar el pedido
    pedido_actual = hacer_pedido(nombre_usuario)

    # Guardar los detalles del pedido en un archivo CSV
    with open('pizzas.csv', 'a') as file:
        # Escribir los detalles del pedido en el archivo CSV
        # Ejemplo:
        file.write(f"{pedido_actual['usuario']}, {pedido_actual['detalles']}\n")
        # Otros detalles del pedido

    print("Pedido realizado y guardado con éxito.")

