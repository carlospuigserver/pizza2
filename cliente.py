import csv
from Builders.masa_builder import MasaPizzaBuilder
from Builders.salsa_builder import SalsaPizzaBuilder
from Builders.ingredientes_builder import IngredientesPizzaBuilder
from Builders.maridajes_builder import BebidaPizzaBuilder
from Builders.coccion_builder import CoccionPizzaBuilder

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

    def elegir_salsa(self, builder):
        print("Tipos de salsa disponibles:")
        tipos_salsa = [
            "Tomate Clásica",
            "Marinara",
            "Pesto",
            "Blanca",
            "BBQ",
            "Champiñones",
            "Tomate sin gluten",
            "Autor",
            "Edición Limitada"
        ]

        print("Elija el tipo de salsa escribiendo su nombre:")
        for tipo in tipos_salsa:
            print(f"- {tipo}")

        tipo_elegido = input("Su elección: ").capitalize()

        if tipo_elegido in tipos_salsa:
            if tipo_elegido == "Tomate Clásica":
                builder.construir_salsa_tomate_clasica()
            elif tipo_elegido == "Marinara":
                builder.construir_salsa_marinara()
            elif tipo_elegido == "Pesto":
                builder.construir_salsa_pesto()
            elif tipo_elegido == "Blanca":
                builder.construir_salsa_blanca()
            elif tipo_elegido == "BBQ":
                builder.construir_salsa_bbq()
            elif tipo_elegido == "Champiñones":
                builder.construir_salsa_champinones()
            elif tipo_elegido == "Tomate sin gluten":
                builder.construir_salsa_tomate_sin_gluten()
            elif tipo_elegido == "Autor":
                builder.construir_salsa_autor()
            else:
                print("Tipo de salsa no válido")
                return None

            return builder.obtener_salsa()

        else:
            print("Tipo de salsa no disponible")
            return None

    def elegir_ingredientes(self, builder):
        while True:
            print("Seleccione los ingredientes para la pizza:")
            builder.anadir_queso()
            builder.anadir_carne()
            builder.anadir_mariscos()
            builder.anadir_vegetales()

            respuesta = input("¿Desea agregar más ingredientes? (Sí/No): ").lower()
            if respuesta != 'sí' and respuesta != 'si':
                break
        return builder.obtener_ingredientes()
    
    def elegir_bebida(self, builder):
        print("Tipos de bebidas disponibles:")
        tipos_bebida = [
            "Vino Blanco",
            "Vino Tinto",
            "Vino Rosado",
            "Cerveza",
            "Coctel"
        ]

        print("Elija el tipo de bebida escribiendo su nombre:")
        for tipo in tipos_bebida:
            print(f"- {tipo}")

        tipo_elegido = input("Su elección: ").capitalize()

        if tipo_elegido == "Vino Blanco":
            builder.construir_vino_blanco()
        elif tipo_elegido == "Vino Tinto":
            builder.construir_vino_tinto()
        elif tipo_elegido == "Vino Rosado":
            builder.construir_vino_rosado()
        elif tipo_elegido == "Cerveza":
            builder.construir_cerveza()
        elif tipo_elegido == "Coctel":
            builder.construir_coctel()
        else:
            print("Tipo de bebida no válido")

        return builder.obtener_bebida()
    
    def elegir_coccion(self, builder):
        print("Métodos de cocción disponibles:")
        metodos_coccion = [
            "Horno de leña",
            "Horno eléctrico",
            "Piedra para pizzas",
            "Parrilla para pizzas"
        ]

        print("Elija el método de cocción escribiendo su nombre:")
        for metodo in metodos_coccion:
            print(f"- {metodo}")

        metodo_elegido = input("Su elección: ").capitalize()

        if metodo_elegido == "Horno de lena":
            builder.construir_horno_lena()
        elif metodo_elegido == "Horno electrico":
            builder.construir_horno_electrico()
        elif metodo_elegido == "Piedra para pizzas":
            builder.construir_piedra_pizzas()
        elif metodo_elegido == "Parrilla para pizzas":
            builder.construir_parrilla_pizzas()
        else:
            print("Método de cocción no válido")

        return builder.obtener_coccion()

    

if __name__ == "__main__":
    masa_builder = MasaPizzaBuilder()
    salsa_builder = SalsaPizzaBuilder()
    ingredientes_builder = IngredientesPizzaBuilder()
    bebida_builder = BebidaPizzaBuilder()
    coccion_builder = CoccionPizzaBuilder()
    cliente = Cliente()

    registrar_nuevo_usuario()  # Registra un nuevo usuario

    nombre_usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")

    if autenticar_usuario(nombre_usuario, contraseña):
        masa_elegida = cliente.elegir_masa(masa_builder)
        if masa_elegida:
            print(f"El usuario {nombre_usuario} ha elegido la masa {masa_elegida.tipo}")

            salsa_elegida = cliente.elegir_salsa(salsa_builder)
            if salsa_elegida:
                print(f"El usuario {nombre_usuario} ha elegido la salsa {salsa_elegida.tipo}")

                ingredientes_elegidos = cliente.elegir_ingredientes(ingredientes_builder)
                if ingredientes_elegidos:
                    print(f"El usuario {nombre_usuario} ha elegido los siguientes ingredientes:")
                    print(ingredientes_elegidos)
                    
                    bebida_elegida = cliente.elegir_bebida(bebida_builder)
                    if bebida_elegida:
                      print(f"El usuario {nombre_usuario} ha elegido la bebida {bebida_elegida.tipo}")

                      coccion_elegida = cliente.elegir_coccion(coccion_builder)
                      if coccion_elegida:
                        print(f"El usuario {nombre_usuario} ha elegido la técnica de cocción {coccion_elegida.metodo}")

                    # Guardar los detalles del pedido en un archivo CSV (pizzas.csv)
                    with open('storage/pizzas.csv', 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([
                            nombre_usuario,
                            f"Elegida masa: {masa_elegida.tipo}",
                            f"Elegida salsa: {salsa_elegida.tipo}",
                            f"Elegidos ingredientes: {ingredientes_elegidos}",
                            f"Elegida bebida: {bebida_elegida.tipo}",
                            f"Elegida tecnica de cocción: {coccion_elegida.metodo}"
                            
                            
                        ])
                    print("Detalles del pedido guardados en pizzas.csv")
