import csv

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
            if row[0] == nombre_usuario and row[1] == contraseña:
                print(f"¡Bienvenido, {nombre_usuario}!")
                return True

    print("Nombre de usuario o contraseña incorrectos.")
    return False

# Registrar un nuevo usuario
registrar_nuevo_usuario()

# Autenticar al usuario con sus credenciales
nombre = input("Nombre de usuario: ")
contraseña = input("Contraseña: ")
autenticar_usuario(nombre, contraseña)
