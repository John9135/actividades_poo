class Personas:
    def __init__(self, nombre_persona, edad, genero):
        self.nombre_persona = nombre_persona
        self.edad = edad
        self.genero = genero

    def presentarse(self):
        print(f"mi nombre es {self.nombre_persona} tengo {self.edad} de edad")


persona = Personas("Alexander Palacio", 12, "Masculino")
persona.presentarse()
