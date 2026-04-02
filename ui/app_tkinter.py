import tkinter as tk
from tkinter import messagebox

# Clase principal de la aplicación
class App:
    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio

        # Título de la ventana
        self.root.title("Lista de Tareas")

       # método para organizar la interfaz
        self._interfaz_configuracion() 

        # Cargar la lista al iniciar
        self.actualizar_lista()
    def _interfaz_configuracion(self):

        # Campo donde el usuario escribe la tarea
        self.entry = tk.Entry(self.root, width=40)
        self.entry.pack(pady=10)

        # Evento Enter para agregar tarea
        self.entry.bind("<Return>", self.agregar_tarea_evento)

        # Botones del sistema
        tk.Button(self.root, text="Añadir Tarea", command=self.agregar_tarea).pack()
        tk.Button(self.root, text="Marcar Completada", command=self.marcar_completada).pack()
        tk.Button(self.root, text="Eliminar", command=self.eliminar_tarea).pack()

        # Lista donde se muestran las tareas
        self.lista = tk.Listbox(self.root, width=50)
        self.lista.pack(pady=10)

        # Evento doble clic
        self.lista.bind("<Double-1>", self.marcar_completada_evento)

        # Atajos de teclado
        self.root.bind("c", self.marcar_completada_evento) # Tecla C completa tarea
        self.root.bind("<Control-d>", self.eliminar_tarea_evento) # Ctrl + D elimina
        self.root.bind("<Escape>", lambda e: self.root.quit())  # Esc cierra app

    # Función para agregar una tarea
    def agregar_tarea(self):
        texto = self.entry.get()

        # Validación simple
        if texto.strip() == "":
            messagebox.showwarning("Aviso", "Escribe una tarea")
            return

        # Se envía al servicio
        self.servicio.agregar_tarea(texto)

        # Limpiar campo
        self.entry.delete(0, tk.END)

        # Actualizar lista
        self.actualizar_lista()

    # Evento ENTER
    def agregar_tarea_evento(self, event):
        self.agregar_tarea()

    # Marcar tarea como completada
    def marcar_completada(self):
        seleccion = self.lista.curselection()

        if seleccion:
            index = seleccion[0]
            tarea = self.servicio.listar_tareas()[index]

            # Uso del getter para obtener el id
            self.servicio.completar_tarea(tarea.get_id())

            self.actualizar_lista()

    # Evento doble clic
    def marcar_completada_evento(self, event):
        self.marcar_completada()

    # Eliminar tarea
    def eliminar_tarea(self):
        seleccion = self.lista.curselection()

        if seleccion:
            index = seleccion[0]
            tarea = self.servicio.listar_tareas()[index]

            # Uso del getter
            self.servicio.eliminar_tarea(tarea.get_id())

            self.actualizar_lista()
    # Evento para eliminar con tecla Delete
    def eliminar_tarea_evento(self, event):
        self.eliminar_tarea()

    # Función que refresca la lista visual
    def actualizar_lista(self):
        self.lista.delete(0, tk.END)

        for tarea in self.servicio.listar_tareas():
            texto = tarea.get_descripcion()

            # Si está completada cambia color
            if tarea.esta_completada():
                self.lista.insert(tk.END, "[Hecho] " + texto)
                self.lista.itemconfig(tk.END, {'fg': 'gray'})
            else:
                self.lista.insert(tk.END, texto)
                self.lista.itemconfig(tk.END, {'fg': 'blue'})
       
            