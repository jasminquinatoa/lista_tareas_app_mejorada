# Clase que representa una tarea
class Tarea:
    def __init__(self, id, descripcion):
        # Atributos privados (encapsulamiento)
        self._id = id
        self._descripcion = descripcion
        self._completada = False

    # Getter para obtener el ID
    def get_id(self):
        return self._id

    # Getter para obtener la descripción
    def get_descripcion(self):
        return self._descripcion

    # Getter para saber si está completada
    def esta_completada(self):
        return self._completada

    # Método para marcar la tarea como completada
    def marcar_completada(self):
        self._completada = True