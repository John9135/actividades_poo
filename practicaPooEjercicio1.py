class Lampara:
    def __init__(self, color_lampara, color_bombilla, anios):
        self.colorLampara = color_lampara
        self.colorBombilla = color_bombilla
        self.anios = anios
        self.esta_encendida = False

    def encender_lampara(self):
        self.esta_encendida = True
        print("La lampara esta encendida")

    def apagar_lampara(self):
        self.esta_encendida = False
        print("La lampara esta apagada")

    def cambiar_bombilla(self, nuevo_color):
        self.color_bombilla = nuevo_color
        print(f"El nuevo color de la bombilla es: {self.color_bombilla}")


lampara1 = Lampara("Verde", "Roja", 22)
print(lampara1.colorLampara, lampara1.colorBombilla, lampara1.anios)

lampara1.cambiar_bombilla("Azul")
lampara1.encender_lampara()
lampara1.apagar_lampara()
