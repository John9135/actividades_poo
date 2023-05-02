class Textos:
    def __init__(self, autor, genero, anio_publicacion, titulo):
        self.autor = autor
        self.genero = genero
        self.anio_publicacion = anio_publicacion
        self.titulo = titulo

    def cambio_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo
        print(f"El titulo estaba equivocado el nuevo titulo es: {self.titulo}")


texto1 = Textos("Maria Ferrei", "Fantasia", "2001", "Roma")
print(texto1.autor, texto1.genero, texto1.anio_publicacion, texto1.titulo)

texto1.cambio_titulo("El nuevo mundo")
