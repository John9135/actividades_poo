class Bebidas:
    def __init__(self, marca, sabor, color, precio):
        self.marca = marca
        self._sabor = sabor
        self.color = color
        self.precio = precio

    def cambio_precio(self, precio):
        self.precio = precio
        print(f"El precio de la bedida cambio a {self.precio}")

    def get_sabor(self):
        return self._sabor

    def set_sabor(self, sabor):
        self._sabor = sabor


class Gaseosa(Bebidas):
    def __init__(self, marca, sabor, color, precio) -> None:
        super().__init__(marca, sabor, color, precio)

    def cambio_precio(self, precio):
        self.precio = precio
        print(f"La gaseosa que quiero toma cuesta {self.precio}")

    def cambiar_sabor(self):
        print(f"Quiero el sabor de {self.get_sabor()}")


class Jugo(Bebidas):
    def __init__(self, marca, sabor, color, precio):
        super().__init__(marca, sabor, color, precio)

    def cambio_precio(self, precio):
        self.precio
        print(f"El jugo cambio de precio es: {self.precio}")


bedida = Bebidas("Postobón", "Manzana", "Rosado", 1200)
print(f"{bedida.marca}, {bedida.get_sabor()}, {bedida.color}, {bedida.precio}")
bedida.cambio_precio(1250)
print()

gaseosa = Gaseosa("Postobon", "Naranja", "Amarillo", 2500)
print(gaseosa.marca, gaseosa.color, gaseosa.get_sabor(), gaseosa.precio)
gaseosa.cambio_precio(1300)
gaseosa.set_sabor("uva")
print(f"El nuevo sabor que quiero es: {gaseosa.get_sabor()} \n")

jugo = Jugo("Hit", "Mandarina", "Amarillo", "4000")
print(jugo.marca, jugo.color, jugo.get_sabor(), jugo.precio)
jugo.cambio_precio(3000)
