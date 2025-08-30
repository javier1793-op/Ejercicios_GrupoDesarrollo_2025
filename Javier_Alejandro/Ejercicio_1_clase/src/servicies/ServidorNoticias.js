class ServidorNoticias {
  constructor() {
    this.noticias = [];
    this.usuarios = [];
  }

  agregarUsuario(usuario) {
    this.usuarios.push(usuario);
  }

  agregarNoticia(noticia) {
    this.noticias.push(noticia);
    return this.notificarUsuarios(noticia);
  }

  notificarUsuarios(noticia) {
    let resultados = [];
    this.usuarios.forEach(usuario => {
      usuario.preferencias.forEach(pref => {
        if (pref.cumple(noticia)) {
          resultados.push(usuario.recibirNoticia(noticia));
        }
      });
    });
    return resultados;
  }
}

module.exports = ServidorNoticias;
