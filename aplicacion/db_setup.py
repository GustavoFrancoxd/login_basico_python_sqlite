import database

#este archivo es opcional, es para agregar un elemento a la base de datos para hacer pruebas

# Crear la tabla si no existe
database.crear_tabla()

# Insertar un usuario de prueba
exito = database.insertar_usuario("Gustavo", "Franco", "gustavofrancoxd@gmail.com", "1234567")
if exito:
    print("Usuario creado exitosamente.")
else:
    print("El usuario ya existe.")
