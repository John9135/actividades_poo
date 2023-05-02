class Cuerpo_celestes:
    def __init__(self, tipo, color, edad):
        self.tipo = tipo
        self.tiene_orbita = True
        self.color = color
        self.edad = edad

    def tiene_orbita_fija(self, orbita):
        if orbita == "si":
            self.tiene_una_orbita = True
            print(f"El cuerpo_celeste {self.tipo} tiene orbita fija")
        else:
            self.tiene_orbita = False
            print(f"El cuerpo celeste {self.tipo} no tiene orbita fija")


cuerpo = Cuerpo_celestes("Estrella", "Rojo", "15'000.000")
print(cuerpo.tipo, cuerpo.color, cuerpo.edad),

print("El cuerpo estelar tiene orbita fija escriba si o no")
orbita = input().lower()

if orbita == "si":
    cuerpo.tiene_orbita = True
else:
    cuerpo.tiene_orbita = False
cuerpo.tiene_orbita_fija(orbita)
