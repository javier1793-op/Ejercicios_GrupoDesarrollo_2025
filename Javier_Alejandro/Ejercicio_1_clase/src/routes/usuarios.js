const express = require("express");
const router = express.Router();
const Usuario = require("../models/Usuario");
const Preferencia = require("../models/Preferencia");

module.exports = (servidor) => {
  // Crear usuario
  router.post("/", (req, res) => {
    const { nombre } = req.body;
    const usuario = new Usuario(nombre);
    servidor.agregarUsuario(usuario);
    res.json({ mensaje: "Usuario creado", usuario });
  });

  // Agregar preferencia
  router.post("/:nombre/preferencias", (req, res) => {
    const { categoriaDeseada, palabrasClave } = req.body;
    const usuario = servidor.usuarios.find(u => u.nombre === req.params.nombre);
    if (!usuario) return res.status(404).json({ error: "Usuario no encontrado" });

    usuario.agregarPreferencia(new Preferencia(categoriaDeseada, palabrasClave));
    res.json({ mensaje: "Preferencia agregada", usuario });
  });

  return router;
};
