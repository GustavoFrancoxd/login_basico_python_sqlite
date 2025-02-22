import tkinter as tk

from sign_up import SignUp
from login import LoginPage
from home import HomePage

class App(tk.Tk):
    """ Clase principal que maneja las ventanas """
    def __init__(self):
        super().__init__()
        self.title("Mi Aplicación")
        self.medida_ventana(300,200)
        self.show_login()  # Mostrar pantalla de login al iniciar


    def medida_ventana(self, x, y):
        """ cambia el tamaño de la ventana """
        self.geometry(f"{x}x{y}")
        self.resizable(False, False)


    def show_login(self):
        """ Muestra la pantalla de login """
        self.clear_screen()
        LoginPage(self)


    def show_home(self, user_email):
        """ Muestra la pantalla de inicio después del login """
        self.clear_screen()
        HomePage(self, user_email)


    def sign_up(self):
        """ Muestra en pantalla formulario registro despues de login"""
        self.clear_screen()
        SignUp(self)


    def clear_screen(self):
        """ Borra los widgets actuales antes de cambiar de pantalla """
        for widget in self.winfo_children():
            widget.destroy()


