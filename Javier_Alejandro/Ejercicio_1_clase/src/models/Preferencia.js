class Preferencia {
  constructor(categoriaDeseada, palabrasClave = []) {
    this.categoriaDeseada = categoriaDeseada;
    this.palabrasClave = palabrasClave;
  }

  cumple(noticia) {
    let cumpleCategoria = noticia.categoria === this.categoriaDeseada;
    let cumplePalabra = this.palabrasClave.every(p => noticia.contienePalabra(p));
    return cumpleCategoria && cumplePalabra;
  }
}

module.exports = Preferencia;
