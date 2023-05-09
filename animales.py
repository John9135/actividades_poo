class Animales:
    def __init__(self, especie, alimentos, habitad, actividad_actual):
        self.especie = especie
        self.alimentos = alimentos
        self.habitad = habitad
        self.actividad_actual = actividad_actual
        self.peligro_extincion = False

    def esta_peligro_extension(self):
        self.peligro_extincion = True
        print("Esta en peligro de extinción")

    def esta_realizando(self, actividad):
        self.actividad_actual = actividad
        print(f"El {self.especie} esta {self.actividad_actual}")


animal1 = Animales("Tigre", "Carne", "Bosque", "Comiendo")
animal1.esta_realizando("Durmiendo")
animal1.esta_peligro_extension()


class Perro(Animales):
    def __init__(self, especie, alimentos, habitad, actividad_actual, nombre_dueño, nombre_dueña):
        self.nombre_dueño = nombre_dueño
        self._nombre_dueña = nombre_dueña
        super().__init__(especie, alimentos, habitad, actividad_actual)

    def nombre_mascota(self, mascotas):
        self._nombre_mascota = mascotas
        print(f"El nombre del hijo {self._nombre_mascota}")

    def esta_realizando(self, actividad):
        self.actividad_actual = actividad
        print(f"{self.nombre_mascota} esta {self.actividad_actual}")

    def get_nombre_dueña(self):
        return self._nombre_dueña

    def set_nombre_dueña(self, nombre_dueña):
        self._nombre_dueña = nombre_dueña


class Gato(Animales):
    def __init__(self, especie, alimentos, habitad, actividad_actual):
        super().__init__(especie, alimentos, habitad, actividad_actual)

    def esta_realizando(self, actividad):
        return super().esta_realizando(actividad)


perro = Perro("Canino", "Cuido", "Urbano", "Jugando", "German", "Laura")
perro.nombre_mascota("Lucky")
perro.set_nombre_dueña("Tatiana")

print(f"La especie del {perro.especie},come {perro.alimentos}, vive en {perro.habitad}, le gusta {perro.actividad_actual}, el nombre del dueños es {perro.nombre_dueño}, El nombre de la dueña es {perro.get_nombre_dueña()}")

perro.esta_realizando("Corriendo")

gato = Gato("Felino", "Cuido", "Hogareño", "Observando")
gato.esta_realizando("Escalando")
