> [!info] Metadatos
> 
> **Fecha:** 2026-08-17
> 
> **Tecnologías:** Docker Compose, Node.js, PostgreSQL, pgAdmin
> 
> **Conceptos:** Multi-contenedor, Variables de Entorno, DNS Interno, Redes Virtuales, Persistencia de Datos.
> 
>   

## 🎯 Objetivo del Proyecto

El objetivo es levantar una arquitectura web real utilizando un solo comando. En lugar de instalar bases de datos y gestores en nuestro PC, usaremos **Docker Compose** para crear una red privada donde coexistan tres servicios:

1. **Una Base de Datos Relacional** (PostgreSQL).
    
2. **Un Panel de Administración Web** (pgAdmin) para gestionar la base de datos visualmente.
    
3. **Una API Backend** (Node.js) que se conecta automáticamente a la base de datos para leer.
    

## 🛠️ Estructura del Proyecto

Para que todo funcione, tu carpeta debe contener exactamente estos **4 archivos**:  

### 1. Las Dependencias (`package.json`)

Define las librerías externas que necesita nuestra API (el framework web y el driver de conexión a la base de datos).

```JSON
{
    "name": "docker-api-pg",
    "main": "server.js",
    "dependencies": {
        "express": "^4.18.2",
        "pg": "^8.11.3"
    }
}
```

### 2. El Manifiesto de la API (`Dockerfile`)

Construye la imagen de nuestro código instalando las dependencias.

```Dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]
```

### 3. El Código Fuente (`server.js`)

Servidor web que usa las variables de entorno inyectadas por Docker para saber dónde conectarse.

```JavaScript
const express = require('express');
const { Pool } = require('pg');

const app = express();
const port = 3000;

// La API lee las credenciales desde el entorno (Variables de Entorno)
const pool = new Pool({
  user: process.env.DB_USER,
  host: process.env.DB_HOST,
  database: process.env.DB_NAME,
  password: process.env.DB_PASSWORD,
  port: process.env.DB_PORT,
});

app.get('/', async (req, res) => {
  try {
    const result = await pool.query('SELECT NOW()');
    res.json({
      mensaje: '¡Conexión exitosa a PostgreSQL desde Docker!',
      hora_base_datos: result.rows[0].now
    });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.listen(port, () => {
  console.log(`API corriendo en puerto ${port}`);
});
```

### 4. El Orquestador (`docker-compose.yml`)

El corazón de la infraestructura. Descarga las imágenes oficiales, compila nuestra API, crea una red virtual que conecta todo y asegura que los datos no se borren.

```YAML
services:
  #1. Gestor de Base de Datos PostgreSQL
  db:
    image: postgres:16-alpine # Seleccionamos la imagen de PostgreSQL
    environment:
      POSTGRES_USER: izan # nombre de usuario
      POSTGRES_PASSWORD: 1234 # contraseña
      POSTGRES_DB: base_tareas # base de datos
    ports:
      - "5432:5432" # Puerto por defecto de PostgreSQL
    volumes:
      - pgdata:/var/lib/postgresql/data # Le dice a Docker que guarde los datos de la base de datos en un volumen llamado 'pgdata'
  
  #2. Gestor Visual de la Base de Datos (Panel Web)
  pgadmin:
    image: dpage/pgadmin4
    environment:
      PGADMIN_DEFAULT_EMAIL: izan@izan.com
      PGADMIN_DEFAULT_PASSWORD: root

    ports:
      - "5050:80" # Puerto para acceder a la interfaz web de pgAdmin
    depends_on:
      - db # Le dice a Docker que espere a que el contenedor 'db' se inicie antes de iniciar 'pgadmin'
    
  #3. Nuestra API Node.js
  api:
    build: .
    ports:
      - "3000:3000"
    environment:
      - DB_HOST=db # nombre del servicio que tiene PostgreSQL
      - DB_USER=izan # nombre de usuario
      - DB_PASSWORD=1234 # contraseña
      - DB_NAME=base_tareas # base de datos
      - DB_PORT=5432 # puerto de PostgreSQL
    depends_on:
      - db # Le dice a Docker que espere a que el contenedor 'db' se inicie antes de iniciar 'api'

# Definimos los volúmenes para PostgreSQL
volumes:
  pgdata: # Definimos el volumen para PostgreSQL
      
```

## 💡 Conceptos Clave Aprendidos

> [!warning] La Indentación en YAML es Crítica
> 
> En archivos `.yml` (como `docker-compose.yml`), los espacios definen la jerarquía. Un error común es colocar los guiones (`- VARIABLE=valor`) a la misma altura que la palabra `environment:`. Deben estar siempre empujados hacia la derecha (2 espacios) para que Docker sepa que pertenecen a esa lista.
> 
>   

> [!tip] DNS Interno Mágico de Docker
> 
> ¿Cómo sabe la API dónde está la base de datos si no le hemos dado ninguna IP?
> 
> En la variable `DB_HOST=db` estamos usando **el nombre del servicio** que definimos en el YAML. Docker Compose crea automáticamente un DNS interno, por lo que el contenedor `api` puede hacer un ping al contenedor `db` simplemente llamándolo por su nombre.
> 
>   

> [!info] Persistencia y Volúmenes
> 
> La directiva `volumes: - pgdata:/var/lib/postgresql/data` toma la carpeta interna donde PostgreSQL guarda las tablas físicas y la vincula a un disco seguro gestionado por Docker (`pgdata`). Si borramos el contenedor de la base de datos y lo volvemos a crear, los datos seguirán intactos.
> 
>   

## 💻 Comandos y Puesta en Marcha

### 1. Levantar toda la infraestructura

Bash

```
docker compose up -d --build
```

_(Se descargarán las imágenes de Postgres y pgAdmin, se compilará la API, y se respetará el orden de arranque dictado por `depends_on`)._

### 2. Rutas de Acceso (Puertos de Izquierda)

- **La API (Node.js):** Entra a `http://localhost:3000` para ver la conexión a la base de datos en formato JSON.
    
- **El Panel de pgAdmin:** Entra a `http://localhost:5050` e inicia sesión con las credenciales que pusimos en el YAML (`izan@izan.com` / `root`).      
    
- **La Base de Datos:** Corre silenciosamente en el puerto `5432` de nuestro equipo para ser accedida por programas externos.
    

### 3. Detener la infraestructura

```Bash
docker compose down
```