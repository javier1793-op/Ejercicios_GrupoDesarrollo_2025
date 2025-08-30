const express = require("express");
const app = express();
app.use(express.json());

const ServidorNoticias = require("./servicies/ServidorNoticias");

const servidor = new ServidorNoticias();

// Rutas
const usuariosRouter = require("./routes/usuarios")(servidor);
const noticiasRouter = require("./routes/noticias")(servidor);

app.use("/usuarios", usuariosRouter);
app.use("/noticias", noticiasRouter);

app.listen(3000, () => {
  console.log("🚀 Servidor corriendo en http://localhost:3000");
});

