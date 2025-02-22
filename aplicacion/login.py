import tkinter as tk
from tkinter import StringVar, messagebox
import database  # Importamos el módulo de base de datos

class LoginPage(tk.Frame):
    """ Pantalla de Login """
    def __init__(self, master):
        super().__init__(master) #el constructor de tk.Frame pide un contenerdor principal como parametro
        self.master = master #es una referencia al contenedor principal
        self.master.title("login")
        self.master.medida_ventana(300, 250) #aqui podemos cambiar todas las propiedades del contenedor principal
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

        # Crear un Label con texto clicable
        texto_clicable = tk.Label(
            self,
            text="Haz clic aquí",
            fg="blue",  # Color del texto
            cursor="hand2",  # Cambia el cursor a una mano
            font=("Arial", 12)  # Fuente y tamaño del texto
        )
        texto_clicable.pack(pady=20)  # Añadir el Label a la ventana

        # Vincular el evento de clic (<Button-1>) a la función al_hacer_clic
        texto_clicable.bind("<Button-1>", lambda event: self.master.sign_up())

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
