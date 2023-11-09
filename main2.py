from Usuario.usuario import *
from Builders.masa_builder import MasaPizzaBuilder
from Builders.salsa_builder import SalsaPizzaBuilder
from Builders.coccion_builder import CoccionPizzaBuilder
from Builders.presentacion_builder import PresentacionPizzaBuilder
from Builders.ingredientes_builder import IngredientesPizzaBuilder
from Builders.extras_builder import ExtrasPizzaBuilder
from Builders.maridajes_builder import BebidaPizza

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
            if len(row) >= 2:  # Verifica si la fila tiene al menos dos elementos
                if row[0] == nombre_usuario and row[1] == contraseña:
                    print(f"¡Bienvenido, {nombre_usuario}!")
                    return True
            else:
                print("Datos incompletos en la fila del archivo CSV.")
                return False

    print("Nombre de usuario o contraseña incorrectos.")
    return False






# Instancia de builders para construir la pizza
masa_builder = MasaPizzaBuilder()
salsa_builder = SalsaPizzaBuilder()
coccion_builder = CoccionPizzaBuilder()
presentacion_builder = PresentacionPizzaBuilder()
ingredientes_builder = IngredientesPizzaBuilder()
extras_builder = ExtrasPizzaBuilder()
maridaje_builder = BebidaPizza()
# Construcción de la pizza
masa = masa_builder.masa_elegida()
salsa = salsa_builder.salsa_elegida()
coccion = coccion_builder.construir_coccion()
presentacion = presentacion_builder.construir_presentacion()
ingredientes = ingredientes_builder.construir_ingredientes()
extras = extras_builder.construir_extras()
maridaje = maridaje_builder.construir_maridaje()

print(f"El usuario {nombre} con contraseña {contraseña} ha elegido una pizza con:\n"
      f"Masa: {masa}\n"
      f"Salsa: {salsa}\n"
      f"Cocción: {coccion}\n"
      f"Presentación: {presentacion}\n"
      f"Ingredientes: {ingredientes}\n"
      f"Extras: {extras}\n"
      f"Bebida para maridar: {maridaje}")
