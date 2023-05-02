class Animales:
    def __init__(self, especie, alimentos, habitad, actividad_actual):
        self.especie = especie
        self.alimentos = alimentos
        self.habitad = habitad
        self.actividad_actual = actividad_actual
        self.peligro_extincion = False
    
    def esta_peligro_extension(self):
        self.peligro_extincion = True
        print ("Esta en peligro de extinción")

    def esta_realizando(self, actividad):
        self.actividad_actual = actividad
        print (f"El {self.especie} esta {self.actividad_actual}")

    
animal1 = Animales("Tigre","Carne","Bosque","Comiendo")

animal1.esta_realizando("Durmiendo")
animal1.esta_peligro_extension()