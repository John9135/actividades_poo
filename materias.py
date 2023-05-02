class Materias:
    def __init__(self, nombre, grado, nombre_profesor):
        self.nombre = nombre
        self.grado = grado
        self.nombre_profesor = nombre_profesor

    def cambio_profesor(self, nombre_p):
        self.nombre_profesor = nombre_p
        print(f"El nuevo profesor se llama {self.nombre_profesor}")


materia = Materias("Matematicas", "8°", "Fernando")
print(materia.nombre, materia.grado, materia.nombre_profesor)

materia.cambio_profesor("Geronimo")
