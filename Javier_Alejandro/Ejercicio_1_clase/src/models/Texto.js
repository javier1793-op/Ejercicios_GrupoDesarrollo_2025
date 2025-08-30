const Contenido = require("./Contenidos");

class Texto extends Contenido {
  constructor(texto) {
    super("Texto");
    this.texto = texto;
  }
}

module.exports = Texto;
