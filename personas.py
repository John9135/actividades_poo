class Personas:
    def __init__(self, nombre_persona, edad, profesion, genero):
        self.nombre_persona = nombre_persona
        self.edad = edad
        self.profesion = profesion
        self.genero = genero

    def presentarse(self):
        print(f"Mi nombre es {self.nombre_persona} tengo {self.edad} de edad")


persona = Personas("Alexander Palacio", 12, "Desarrollador", "Masculino")
persona.presentarse()


# ----------------------------------------------------------------------------------
class Alumnos(Personas):
    def __init__(self, nombre_persona, edad, profesion, genero, grado):
        super().__init__(nombre_persona, edad, profesion, genero)
        self.grado = grado

    def horario(self, hora_inicio, hora_final):
        self._hora_inicio = hora_inicio
        self._hora_final = hora_final
        print(
            f"El horario de estuio es de {self._hora_inicio} a {self._hora_final}")

    def director_de_grupo(self, nombre_persona, nombre_materia):
        self._nombre_persona = nombre_persona
        self._nombre_materia = nombre_materia

        print(
            f"El director de grupo se llama {self._nombre_persona} y la materia que enseña es {self._nombre_materia}")

    def get_hora_inicio(self):
        return self._hora_inicio

    def set_hora_inicio(self, hora_inicio):
        self._hora_inicio = hora_inicio

    def get_hora_final(self):
        return self._hora_final

    def set_hora_final(self, hora_final):
        self._hora_final = hora_final

    def get_nombre_profesor(self):
        return self._nombre_profesor

    def set_nombre_profesor(self, nombre_profesor):
        self._nombre_profesor = nombre_profesor


alumno = Alumnos("Fernanda Zuluaga", 10, "Estudiante", "Femenino", "5°")
print(alumno.nombre_persona, alumno.edad,
      alumno.profesion, alumno.genero, alumno.grado)


alumno.presentarse()
alumno.horario("12:00pm", "5:00pm")

alumno.set_hora_final("6:00pm")
alumno.set_hora_inicio("1:00pm")
print(
    f"El horario de entrada cambio a {alumno.get_hora_inicio()} el horario de salida cambio {alumno.get_hora_final()}")

alumno.director_de_grupo("Salome Zapata", "Ciencias sociales")
alumno.set_nombre_profesor("Laura Torres")
print(f"El nombre del director nuevo es {alumno.get_nombre_profesor()}")
