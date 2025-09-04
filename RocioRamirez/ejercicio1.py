from abc import ABC, abstractmethod
from datetime import date

# ----- Contenido y derivados -----
class Contenido(ABC):
    @abstractmethod
    def get(self):
        pass

class Texto(Contenido):
    def __init__(self, contenido):
        self.contenido = contenido

    def get(self):
        return self.contenido

class Imagen(Contenido):
    def __init__(self, resolucion):
        self.resolucion = resolucion

    def get(self):
        return f"Imagen de resolución {self.resolucion}"

class Video(Contenido):
    def __init__(self, duracion):
        self.duracion = duracion

    def get(self):
        return f"Video de duración {self.duracion}"

# ----- CuerpoNoticia -----
class CuerpoNoticia:
    def __init__(self, id_cuerpo, fecha_creacion):
        self.idCuerpo = id_cuerpo
        self.fechaCreacion = fecha_creacion
        self.listaContenido = []

    def agregar_contenido(self, contenido):
        self.listaContenido.append(contenido)

    def get(self):
        return [c.get() for c in self.listaContenido]

    def contar_palabras(self):
        total = 0
        for c in self.listaContenido:
            if isinstance(c, Texto):
                total += len(c.contenido.split())
        return total

    def contiene_palabra(self, palabra):
        for c in self.listaContenido:
            if isinstance(c, Texto) and palabra in c.contenido:
                return True
        return False

    def contiene_lista_palabras(self, lista):
        for palabra in lista:
            if not self.contiene_palabra(palabra):
                return False
        return True

# ----- Categoria -----
class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

# ----- Noticia -----
class Noticia:
    def __init__(self, titulo, categoria, cuerpo):
        self.titulo = titulo
        self.categoria = categoria
        self.cuerpo = cuerpo

    def contar_palabras(self):
        return self.cuerpo.contar_palabras()

    def contiene_palabra(self, palabra):
        return self.cuerpo.contiene_palabra(palabra)

    def contiene_lista_palabras(self, lista):
        return self.cuerpo.contiene_lista_palabras(lista)

# ----- Filtros -----
class Filtro(ABC):
    @abstractmethod
    def cumple(self, noticia):
        pass

class FiltroTitulo(Filtro):
    def __init__(self, frase):
        self.frase = frase

    def cumple(self, noticia):
        return noticia.titulo == self.frase

class FiltroCategoria(Filtro):
    def __init__(self, categoria):
        self.categoria = categoria

    def cumple(self, noticia):
        return noticia.categoria == self.categoria

class FiltroPalabra(Filtro):
    def __init__(self, palabra):
        self.palabra = palabra

    def cumple(self, noticia):
        return noticia.contiene_palabra(self.palabra)

class FiltroListaPalabras(Filtro):
    def __init__(self, lista_palabras):
        self.lista_palabras = lista_palabras

    def cumple(self, noticia):
        return noticia.contiene_lista_palabras(self.lista_palabras)

class FiltroCantidadPalabras(Filtro):
    def __init__(self, max_palabras):
        self.max_palabras = max_palabras

    def cumple(self, noticia):
        return noticia.contar_palabras() <= self.max_palabras

# ----- Suscripcion -----
class Suscripcion:
    def __init__(self, filtro):
        self.filtro = filtro

    def cumple(self, noticia):
        return self.filtro.cumple(noticia)

# ----- Usuario -----
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.suscripcion = None

    def agregar_suscripcion(self, suscripcion):
        self.suscripcion = suscripcion

    def recibir_noticia(self, noticia):
        print(f"{self.nombre} recibió la noticia: {noticia.titulo}")

# ----- ServidorNoticias -----
class ServidorNoticias:
    def __init__(self):
        self.noticias = []
        self.suscriptores = []

    def agregar_noticia(self, noticia):
        self.noticias.append(noticia)
        # Notificar a los suscriptores
        for usuario in self.suscriptores:
            if usuario.suscripcion and usuario.suscripcion.cumple(noticia):
                usuario.recibir_noticia(noticia)

    def buscar(self, filtro):
        return [n for n in self.noticias if filtro.cumple(n)]

    def suscribir(self, usuario, suscripcion):
        usuario.agregar_suscripcion(suscripcion)
        if usuario not in self.suscriptores:
            self.suscriptores.append(usuario)

# ----- Ejemplo de uso -----
if __name__ == "__main__":
    # Crear contenidos
    texto = Texto("De Paul fue figura en la final de deportes.")
    imagen = Imagen(1080)
    video = Video("00:02:30")

    # Crear cuerpo de noticia
    cuerpo = CuerpoNoticia(1, date.today())
    cuerpo.agregar_contenido(texto)
    cuerpo.agregar_contenido(imagen)
    cuerpo.agregar_contenido(video)

    # Crear noticia
    categoria = Categoria("deportes")
    noticia = Noticia("Gran Final", categoria, cuerpo)

    # Crear usuario y suscripción
    usuario = Usuario("Valeria")
    filtro = FiltroCategoria(categoria)
    suscripcion = Suscripcion(filtro)

    # Crear servidor y suscribir usuario
    servidor = ServidorNoticias()
    servidor.suscribir(usuario, suscripcion)

    # Agregar noticia (usuario recibe la noticia si cumple el filtro)
    servidor.agregar_noticia(noticia)

