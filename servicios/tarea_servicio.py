# Importamos el modelo
from modelos.tarea import Tarea

# Clase que maneja la lógica de negocio
class TareaServicio:
    def __init__(self):
        # Lista de tareas
        self.tareas = []
        
        # Contador para IDs únicos
        self.contador = 0

    # Método para agregar tarea
    def agregar_tarea(self, descripcion):
        self.contador += 1
        nueva_tarea = Tarea(self.contador, descripcion)
        self.tareas.append(nueva_tarea)

    # Método para listar tareas
    def listar_tareas(self):
        return self.tareas

    # Método para completar tarea
    def completar_tarea(self, id):
        for tarea in self.tareas:
            if tarea.get_id() == id:
                tarea.marcar_completada()

    # Método para eliminar tarea
    def eliminar_tarea(self, id):
        self.tareas = [t for t in self.tareas if t.get_id() != id]