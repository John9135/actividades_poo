class Textos:
    def __init__(self, autor, genero, anio_publicacion, titulo):
        self.autor = autor
        self.genero = genero
        self.anio_publicacion = anio_publicacion
        self.titulo = titulo

    def cambio_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo
        print(f"El titulo estaba equivocado el nuevo titulo es: {self.titulo}")


class Pergamino(Textos):
    def __init__(self, autor, genero, anio_publicacion, titulo, antiguedad):
        self._antiguedad = antiguedad
        super().__init__(autor, genero, anio_publicacion, titulo)

    def cambio_antiguedad(self):
        print("Escriba la antiguedad del pergamino")
        antiguedad = input()
        self.set_antiguedad = antiguedad
        print(f"La antiguedad de este pergamino es de {self.set_antiguedad}")

    def get_antiguedad(self):
        return self._antiguedad

    def set_antiguedad(self, antiguedad):
        self._antiguedad = antiguedad


texto1 = Textos("Maria Ferrei", "Fantasia", "2001", "Roma")
print(texto1.autor, texto1.genero, texto1.anio_publicacion, texto1.titulo)
texto1.cambio_titulo("El nuevo mundo")

pergamino = Pergamino("Desconocido", "Religión", "19 a.c", "Ra", 3000)
print(pergamino.autor, pergamino.genero,
      pergamino.anio_publicacion, pergamino.get_antiguedad())

pergamino.cambio_titulo("Historia de RA")
pergamino.cambio_antiguedad()
