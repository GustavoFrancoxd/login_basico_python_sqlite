import tkinter as tk
from tkinter import StringVar, messagebox
import database  # Importamos el módulo de base de datos

class LoginPage(tk.Frame):
    """ Pantalla de Login """
    def __init__(self, master):
        super().__init__(master) #el constructor de tk.Frame pide un contenerdor principal como parametro
        self.master = master #es una referencia al contenedor principal
        self.master.medida_ventana(300, 200) #aqui podemos cambiar todas las propiedades del contenedor principal
        self.pack(pady=20)

        # Variables
        self.usuario = StringVar()
        self.contrasena = StringVar()

        # UI
        #el primer parametro es donde se van a almacenar
        tk.Label(self, text="Usuario: ").pack(pady=5)
        tk.Entry(self, textvariable=self.usuario, width=30).pack()

        tk.Label(self, text="Contraseña: ").pack(pady=5)
        tk.Entry(self, textvariable=self.contrasena, show="*", width=30).pack()

        tk.Button(self, text="Iniciar sesión", command=self.ingresar).pack(pady=10)

    def ingresar(self):
        """ Verifica credenciales y cambia de pantalla si son correctas """
        email_ingresado = self.usuario.get().strip()
        password_ingresado = self.contrasena.get().strip()

        if not email_ingresado or not password_ingresado:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        resultado = database.obtener_usuario(email_ingresado)  # Consultamos la base de datos

        if resultado is None:
            messagebox.showerror("Error", "Usuario no encontrado.")
        elif password_ingresado == resultado[0]:
            messagebox.showinfo("Bienvenido", f"Hola, {email_ingresado}!")
            self.master.show_home(email_ingresado)  # Cambia a la pantalla de inicio
        else:
            messagebox.showerror("Error", "Contraseña incorrecta.")
