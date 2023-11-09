import csv
from Builders.masa_builder import MasaPizzaBuilder

# Función para registrar un nuevo usuario
def registrar_nuevo_usuario():
    nombre_usuario = input("Introduce tu nombre de usuario: ")
    contraseña = input("Introduce tu contraseña: ")

    with open('Usuario/usuario.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nombre_usuario, contraseña])
        print(f"El usuario '{nombre_usuario}' se ha registrado con éxito.")

# Función para autenticar un usuario
def autenticar_usuario(nombre_usuario, contraseña):
    with open('Usuario/usuario.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:  # Verifica si la lista tiene al menos dos elementos
                if row[0] == nombre_usuario and row[1] == contraseña:
                    print(f"¡Bienvenido, {nombre_usuario}!")
                    return True

    print("Nombre de usuario o contraseña incorrectos.")
    return False

class Cliente:
    def elegir_masa(self, builder):
        print("Tipos de masa disponibles:")
        tipos_masa = [
            "Delgada",
            "48 Horas",
            "Madre",
            "Poolish",
            "Napolitana",
            "New York Style",
            "Chicago Style",
            "Siciliana",
            "Cracker"
        ]

        print("Elija el tipo de masa escribiendo su nombre:")
        for tipo in tipos_masa:
            print(f"- {tipo}")

        tipo_elegido = input("Su elección: ").capitalize()

        if tipo_elegido in tipos_masa:
            if tipo_elegido == "Delgada":
                builder.construir_masa_delgada()
            # Resto de lógica para construir el tipo de masa
            # builder.construir_masa_tipo_elegido() u otro similar
            masa = builder.obtener_masa()  # Obtener la masa construida
            masa.tipo = tipo_elegido  # Asignar el tipo de masa elegida
            return masa  # Devolver la masa creada y asignada con el tipo

        else:
            print("Tipo de masa no disponible")
            return None

if __name__ == "__main__":
    builder = MasaPizzaBuilder()

    registrar_nuevo_usuario()  # Registra un nuevo usuario

    nombre_usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")

    cliente = Cliente()
    if autenticar_usuario(nombre_usuario, contraseña):
        masa_elegida = cliente.elegir_masa(builder)
        if masa_elegida:
            print(f"El usuario {nombre_usuario} ha elegido la masa {masa_elegida.tipo}")

            # Guardar los detalles del pedido en un archivo CSV (pizzas.csv)
            with open('storage/pizzas.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([nombre_usuario, f"Elegida masa: {masa_elegida.tipo}"])
                print("Detalles del pedido guardados en pizzas.csv")