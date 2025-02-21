import sqlite3

DB_NAME = "login"

def conectar():
    """ Conecta a la base de datos y devuelve la conexión y el cursor """
    con = sqlite3.connect(DB_NAME)
    cursor = con.cursor()
    return con, cursor


def crear_tabla():
    """ Crea la tabla de usuarios si no existe """
    con, cursor = conectar()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    con.commit()
    con.close()


def insertar_usuario(nombre, apellido, email, password):
    """ Inserta un nuevo usuario en la base de datos """
    con, cursor = conectar()
    try:
        cursor.execute("INSERT INTO usuario (nombre, apellido, email, password) VALUES (?, ?, ?, ?)",
                       (nombre, apellido, email, password))
        con.commit()
        return True
    except sqlite3.IntegrityError:
        return False  # Si el email ya existe
    finally:
        con.close()


def obtener_usuario(email):
    """ Busca un usuario por email y devuelve su contraseña """
    con, cursor = conectar()
    cursor.execute("SELECT password FROM usuario WHERE email = ?", (email,))
    resultado = cursor.fetchone()
    con.close()
    return resultado
