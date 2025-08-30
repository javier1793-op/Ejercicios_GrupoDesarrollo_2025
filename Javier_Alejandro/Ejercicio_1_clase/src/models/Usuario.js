class Usuario {
  constructor(nombre) {
    this.nombre = nombre;
    this.preferencias = [];
  }

  agregarPreferencia(pref) {
    this.preferencias.push(pref);
  }

  recibirNoticia(noticia) {
    return `📩 Usuario ${this.nombre} recibió noticia: ${noticia.titulo}`;
  }
}

module.exports = Usuario;
