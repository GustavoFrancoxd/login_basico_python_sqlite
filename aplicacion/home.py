import tkinter as tk

class HomePage(tk.Frame):
    """ Pantalla de inicio después del login """
    def __init__(self, master, user_email):
        super().__init__(master)
        self.master = master
        self.master.medida_ventana(600, 600)
        self.pack()


        tk.Label(self, text=f"Bienvenido, {user_email}!", font=("Arial", 14)).pack()
        tk.Button(self, text="Cerrar sesión", command=self.master.show_login).pack()
