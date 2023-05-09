class Cuerpo_celestes:
    def __init__(self, tipo, color, edad):
        self._tipo = tipo
        self.tiene_orbita = True
        self.color = color
        self.edad = edad

    def tiene_orbita_fija(self):
        print("El cuerpo estelar tiene orbita fija escriba si o no")
        orbita = input().lower()

        if orbita == "si":
            self.tiene_una_orbita = True
            print(f"El cuerpo_celeste {self._tipo} tiene orbita fija \n")
        else:
            self.tiene_orbita = False
            print(f"El cuerpo celeste {self._tipo} no tiene orbita fija \n")

    def get_tipo(self):
        return self._tipo

    def set_tipo(self, tipo):
        self._tipo = tipo


class Planeta(Cuerpo_celestes):
    def __init__(self, tipo, color, edad, tiene_vida):
        self.tiene_vida = tiene_vida
        super().__init__(tipo, color, edad)

    def gira_sobre_su_eje(self):
        print("Gira sobre su propio eje")


cuerpo = Cuerpo_celestes("Estrella", "Rojo", "15'000.000")
print(cuerpo.get_tipo(), cuerpo.color, cuerpo.edad + "\n"),
cuerpo.tiene_orbita_fija()

planeta = Planeta("planeta", "Azul", "1'000.000", "si")
print(planeta.get_tipo(), planeta.color, planeta.edad)
planeta.set_tipo("Cometa")
print(planeta.get_tipo())
planeta.gira_sobre_su_eje()
planeta.tiene_orbita_fija()
