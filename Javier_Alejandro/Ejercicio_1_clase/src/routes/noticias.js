const express = require("express");
const router = express.Router();
const Noticia = require("../models/Noticia");
const Texto = require("../models/Texto");

module.exports = (servidor) => {
  // Crear noticia
  router.post("/", (req, res) => {
    const { titulo, categoria, texto } = req.body;
    const noticia = new Noticia(titulo, categoria, new Texto(texto));
    const notificados = servidor.agregarNoticia(noticia);
    res.json({ mensaje: "Noticia agregada", noticia, notificados });
  });

  // Listar todas las noticias
  router.get("/", (req, res) => {
    res.json(servidor.noticias);
  });

  return router;
};
