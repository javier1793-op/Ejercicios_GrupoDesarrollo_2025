const Texto = require("./Texto");

class Noticia {
  constructor(titulo, categoria, contenido) {
    this.titulo = titulo;
    this.categoria = categoria;
    this.contenido = contenido;
  }

  contienePalabra(palabra) {
    if (this.contenido instanceof Texto) {
      return this.contenido.texto.includes(palabra);
    }
    return false;
  }
}

module.exports = Noticia;

