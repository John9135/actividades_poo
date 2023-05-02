class Bebidas:
    def __init__(self, marca, sabor, color, precio) -> None:
        self.marca = marca
        self.sabor = sabor
        self.color = color
        self.precio = precio

    def cambio_precio(self, precio):
        self.precio = precio
        print(f"El preio de la bedida cambio a {self.precio}")


bedida = Bebidas("Postobón", "Manzana", "Rosaso", 1200)
print(f"{bedida.marca}, {bedida.sabor}, {bedida.color}, {bedida.precio}")

bedida.cambio_precio(1250)
