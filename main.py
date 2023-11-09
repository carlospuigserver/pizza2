# main.py
from Builders.masa_builder import MasaPizzaBuilder
from Builders.salsa_builder import SalsaPizzaBuilder
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
    # Otros builders para ingredientes, cocción, presentación, maridaje, extras...

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
    # Otras elecciones y construcción de la pizza...

    # Guardar los detalles de la pizza en un archivo CSV
    pizza_details = {
        'Masa': masa.tipo,
        'Salsa': salsa.tipo,
        # Otros detalles de la pizza
    }

    # Agregar la pizza al archivo CSV
    csv_handler_pizzas = CSVHandler('pizzas.csv')
    csv_handler_pizzas.guardar_pizza(pizza_details)
