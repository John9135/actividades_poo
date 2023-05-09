class Materias:
    def __init__(self, nombre_materia, grado, nombre_profesor):
        self._nombre_materia = nombre_materia
        self.grado = grado
        self.nombre_profesor = nombre_profesor

    def cambio_profesor(self, nombre_p):
        self.nombre_profesor = nombre_p
        print(f"El nuevo profesor se llama {self.nombre_profesor}")

    def get_nombre_materia(self):
        return self._nombre_materia

    def set_nombre_materia(self, materia):
        self._nombre_materia = materia


class Matematicas(Materias):
    def __init__(self, nombre_materia, grado, nombre_profesor):
        super().__init__(nombre_materia, grado, nombre_profesor)

    def nuevo_nombre(self):
        print(f"El nuevo nombre de la materia es {self.get_nombre_materia()}")


materia = Matematicas("Matematicas", "8°", "Fernando")
print(materia.get_nombre_materia(), materia.grado, materia.nombre_profesor)
materia.cambio_profesor("Geronimo")
materia.set_nombre_materia("Matematicas IV")
materia.nuevo_nombre()
