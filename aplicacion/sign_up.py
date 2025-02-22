import tkinter as tk
from tkinter import StringVar, messagebox

from tomlkit import string

from aplicacion.database import insertar_usuario


class SignUp(tk.Frame):
    """ Pantalla para registrarse """
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Sign up")
        self.master.medida_ventana(300, 250)
        self.pack()

        self.nombre = StringVar()
        self.apellido = StringVar()
        self.correo = StringVar()
        self.contrasena = StringVar()

        # Crear y colocar los labels y entries en un grid de 2x2
        # Fila 0
        label_nombre = tk.Label(self, text="Nombre:")
        label_nombre.grid(row=0, column=0, padx=10, pady=10)

        entry_nombre = tk.Entry(self, textvariable=self.nombre)
        entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        # Fila 1
        label_apellido = tk.Label(self, text="Apellido:")
        label_apellido.grid(row=1, column=0, padx=10, pady=10)

        entry_apellido = tk.Entry(self, textvariable=self.apellido)
        entry_apellido.grid(row=1, column=1, padx=10, pady=10)

        # Fila 2
        label_correo = tk.Label(self, text="Correo:")
        label_correo.grid(row=2, column=0, padx=10, pady=10)

        entry_correo = tk.Entry(self, textvariable=self.correo)
        entry_correo.grid(row=2, column=1, padx=10, pady=10)

        # Fila 3
        label_contrasena = tk.Label(self, text="Contraseña:")
        label_contrasena.grid(row=3, column=0, padx=10, pady=10)

        entry_contrasena = tk.Entry(self, show="*", textvariable=self.contrasena)  # Para ocultar la contraseña
        entry_contrasena.grid(row=3, column=1, padx=10, pady=10)

        tk.Button(self, text="regresar", command=self.master.show_login).grid(row=4, column=0, pady=10)

        tk.Button(self, text="Registrarse", command=self.registrar).grid(row=4, column=1, pady=10)

    def registrar(self):
        """ Guarda los datos del usuario """
        nombre = self.nombre.get().strip()
        apellido = self.apellido.get().strip()
        correo = self.correo.get().strip()
        contrasena = self.contrasena.get().strip()

        if not nombre or not apellido or not correo or not contrasena:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        # Aquí puedes guardar los datos en la base de datos
        if insertar_usuario(nombre, apellido, correo, contrasena):
            messagebox.showinfo("Éxito", "Registro exitoso.")
        else:
            messagebox.showerror("Error", "Error al realizar registro en base de datos")

        self.master.show_login()  # Regresa a la pantalla de login
