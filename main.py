# Archivo principal que inicia la aplicación

import tkinter as tk
from servicios.tarea_servicio import TareaServicio
from ui.app_tkinter import App

# Punto de entrada del programa
if __name__ == "__main__":
    
    # Crear ventana principal
    root = tk.Tk()
    
    # Crear el servicio (lógica del sistema)
    servicio = TareaServicio()
    
    # Crear la aplicación gráfica
    app = App(root, servicio)
    
    # Ejecutar la aplicación
    root.mainloop()