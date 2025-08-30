# Servidor de Noticias Node.js

Este proyecto es un **servidor de noticias** construido con **Node.js y Express**, que permite:  

- Crear usuarios y agregar preferencias por categoría y palabras clave.  
- Crear noticias con contenido de texto.  
- Notificar automáticamente a los usuarios cuando se publica una noticia que cumple sus preferencias.  

El proyecto está organizado en carpetas para una mejor estructura y escalabilidad:  

- /src
- /models
- Contenido.js
- Texto.js
- Noticia.js
- Preferencia.js
- Usuario.js
- /services
- ServidorNoticias.js
- /routes
- usuarios.js
- noticias.js
- server.js

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/javier1793-op/ServidorNoticias.git
cd EJERCICIO CLASE

npm install

node src/server.js
El servidor correrá en http://localhost:3000.

## Rutas de la API
Usuarios

Crear usuario

POST /usuarios
Body: { "nombre": "NombreDelUsuario" }


Agregar preferencia a un usuario

POST /usuarios/:nombre/preferencias
Body: { 
  "categoriaDeseada": "Deportes", 
  "palabrasClave": ["fútbol", "liga"] 
}

Noticias

Crear noticia

POST /noticias
Body: { 
  "titulo": "Título de la noticia", 
  "categoria": "Deportes", 
  "texto": "Contenido de la noticia..." 
}


## Listar todas las noticias

GET /noticias

Ejemplo de flujo

Crear usuario "Javier".

Agregar preferencia: categoría "Tecnología", palabras clave ["Node", "Express"].

Crear noticia con categoría "Tecnología" y contenido que incluya "Node".

El servidor notificará automáticamente al usuario "Javier".

