> [!info] Metadatos 
> **Lenguaje:** Python 3.12 (FastAPI) 
> **Base de Datos:** MySQL 8.0 
> **Extras:** Auto-generación de Docs (Swagger), Adminer, Auto-creación de tablas.
> 
**Objetivo:** Entender la orquestación de contenedores, la comunicación entre servicios y la diferencia entre herramientas de administración visuales y peticiones a una API.

## 🧠 1. Arquitectura y Conceptos Clave

Antes del código, es vital entender cómo se comunican las piezas y resolver dudas comunes sobre esta infraestructura.

### 🏦 Adminer vs API (La metáfora del Banco)

- **MySQL (La Bóveda):** Es el único que guarda datos físicamente en el disco duro. Solo escucha peticiones por el puerto 3306.
 
- **Adminer (El Director del Banco):** Es una interfaz visual conectada a MySQL. Tiene acceso total. Puedes crear tablas a mano, borrar la base de datos o editar registros directamente. Lo que hagas aquí va directo a MySQL, saltándose la API.
 
- **API Python + Swagger (El Cajero Automático):** Es un puente programado para que aplicaciones o usuarios externos interactúen con la base de datos de forma controlada. Si la API no tiene programado un `DELETE`, nadie podrá borrar datos usándola. Swagger es solo la pantalla táctil de este cajero automático para hacer pruebas sin programar un frontend.
 

### 🌐 ¿Por qué no puedo crear un libro desde la URL del navegador?

Si escribes `http://localhost:8000/libros` en la barra superior de Chrome y pulsas Enter, el navegador **siempre lanza una petición `GET`** (Leer). Para crear un libro, la API exige un método **`POST`**. Para hacer un `POST` necesitas:

1. **Swagger UI:** Entrando en `/docs` y usando el botón visual de "Try it out".
 
2. **Terminal:** Usando comandos como `curl -X 'POST'...`
 
3. **Clientes de API:** Programas como Postman o Thunder Client.
 

### 🐳 Entendiendo el Dockerfile de Python

- **`--no-cache-dir`:** A diferencia de Node.js, `pip` guarda los instaladores descargados en una caché oculta. En Docker, el espacio es oro. Este comando instala la librería y borra la caché inmediatamente para que la imagen pese menos.

![[🐍 API REST (FastAPI) + MySQL + Adminer.png]]


- **El comando `CMD`:** FastAPI no tiene servidor web integrado. Usamos `uvicorn`. Es vital el parámetro `--host 0.0.0.0` para que el contenedor abra sus puertas al exterior (tu PC), de lo contrario solo escucharía tráfico interno (`127.0.0.1`) y no podrías acceder desde tu navegador.
 

## 🎯 2. Estructura de Archivos

Crea una carpeta nueva y añade estos **4 archivos**:

### 1. Las Dependencias (`requirements.txt`)

El equivalente al `package.json` de Node.

```Plaintext
fastapi
uvicorn
pymysql
```

### 2. El Manifiesto (`Dockerfile`)

Construye la imagen de la API.



```Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt.

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py.

EXPOSE 8000

# Ejecutamos el servidor Uvicorn en el puerto 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

### 3. El Código de la API (`main.py`)

Implementa el CRUD y crea la tabla en la base de datos si no existe.

```Python
from fastapi import FastAPI, HTTPException
import pymysql
import os

app = FastAPI(title="API de Biblioteca Personal")

# Función para conectarse a MySQL leyendo el docker-compose
def get_db_connection():
 return pymysql.connect(
 host=os.getenv("DB_HOST", "db"),
 user=os.getenv("DB_USER", "izan"),
 password=os.getenv("DB_PASSWORD", "1234"),
 database=os.getenv("DB_NAME", "biblioteca"),
 cursorclass=pymysql.cursors.DictCursor
 )

# --- INICIALIZACIÓN ---
@app.on_event("startup")
def startup():
 # Crea la tabla de libros automáticamente al arrancar
 conn = get_db_connection()
 with conn.cursor() as cursor:
 cursor.execute("""
 CREATE TABLE IF NOT EXISTS libros (
 id INT AUTO_INCREMENT PRIMARY KEY,
 titulo VARCHAR(255) NOT NULL,
 autor VARCHAR(255) NOT NULL,
 leido BOOLEAN DEFAULT FALSE
 )
 """)
 conn.commit()
 conn.close()

# --- CRUD ENDPOINTS ---

@app.get("/libros")
def obtener_libros():
 conn = get_db_connection()
 with conn.cursor() as cursor:
 cursor.execute("SELECT * FROM libros")
 libros = cursor.fetchall()
 conn.close()
 return libros

@app.post("/libros")
def crear_libro(titulo: str, autor: str):
 conn = get_db_connection()
 with conn.cursor() as cursor:
 cursor.execute("INSERT INTO libros (titulo, autor) VALUES (%s, %s)", (titulo, autor))
 nuevo_id = cursor.lastrowid
 conn.commit()
 conn.close()
 return {"mensaje": "Libro añadido con éxito", "id": nuevo_id, "titulo": titulo}

@app.put("/libros/{libro_id}")
def marcar_leido(libro_id: int, leido: bool):
 conn = get_db_connection()
 with conn.cursor() as cursor:
 cursor.execute("UPDATE libros SET leido = %s WHERE id = %s", (leido, libro_id))
 filas_afectadas = cursor.rowcount
 conn.commit()
 conn.close()
 
 if filas_afectadas == 0:
 raise HTTPException(status_code=404, detail="Libro no encontrado")
 return {"mensaje": f"Libro {libro_id} actualizado"}

@app.delete("/libros/{libro_id}")
def borrar_libro(libro_id: int):
 conn = get_db_connection()
 with conn.cursor() as cursor:
 cursor.execute("DELETE FROM libros WHERE id = %s", (libro_id,))
 filas_afectadas = cursor.rowcount
 conn.commit()
 conn.close()

 if filas_afectadas == 0:
 raise HTTPException(status_code=404, detail="Libro no encontrado")
 return {"mensaje": "Libro eliminado correctamente"}
```

### 4. El Orquestador (`docker-compose.yml`)

Levanta los tres contenedores. Incluye `restart: always` para solucionar posibles caídas.

```YAML
services:
 # 1. Base de Datos MySQL
 db:
 image: mysql:8.0
 environment:
 MYSQL_ROOT_PASSWORD: root
 MYSQL_DATABASE: biblioteca
 MYSQL_USER: izan
 MYSQL_PASSWORD: 1234
 ports:
 - "3306:3306"
 volumes:
 - dbBiblioteca:/var/lib/mysql

 # 2. Adminer (Panel visual de MySQL)
 adminer:
 image: adminer
 ports:
 - "8080:8080"
 depends_on:
 - db

 # 3. API en Python (FastAPI)
 api:
 build:.
 restart: always 
 ports:
 - "8000:8000"
 environment:
 - DB_HOST=db
 - DB_USER=izan
 - DB_PASSWORD=1234
 - DB_NAME=biblioteca
 depends_on:
 - db
 volumes:
 -.:/app # Hot-reload para Python

volumes:
 dbBiblioteca:
```

## 🚀 3. Ejecución y Pruebas

### Levantar la infraestructura

Abre la terminal en la carpeta del proyecto y ejecuta:

```Bash
docker compose up -d --build
```

> [!warning]
> La Condición de Carrera MySQL tarda unos 10-15 segundos en inicializarse. Como la API de Python es rapidísima, puede que intente conectarse antes de que la DB esté lista y el contenedor se apague. Gracias al `restart: always` en el `docker-compose.yml`, Docker reiniciará la API automáticamente hasta que enganche con MySQL.

### Probar la API (Swagger UI)

1. Ve a tu navegador y entra en `http://localhost:8000/docs`.
 
2. Despliega el método **POST /libros**.
 
3. Pulsa en **"Try it out"**.
 
4. Rellena los campos:
 
 - **titulo:** Meditaciones
 
 - **autor:** Marco Aurelio
 
5. Pulsa **Execute**. Deberías recibir un código 200 confirmando la inserción.
 

### Verificar la Base de Datos (Adminer)

1. Abre `http://localhost:8080`.
 
2. **Sistema:** MySQL | **Servidor:** `db` | **Usuario:** `izan` | **Contraseña:** `1234` | **Base de datos:** `biblioteca`
 
3. Entra en la tabla `libros` y comprueba que el registro se ha guardado correctamente a través de la API.
 

## 🛠️ 4. Solución de Problemas (Troubleshooting)

### Error: "ports are not available... bind: Solo se permite un uso de cada dirección de socket"

- **Causa:** El puerto 3306 de tu ordenador ya está siendo usado por un servicio local de Windows (XAMPP, instalación nativa de MySQL, etc.).
 
- **Solución A:** Detener el servicio local de MySQL desde la herramienta "Servicios" de Windows.
 
- **Solución B:** Cambiar el puerto en el `docker-compose.yml` (`ports: - "3307:3306"`).
 

### Líneas rojas en el IDE (Error de Linter: "Could not find name 'pymysql'")

- **Causa:** El editor (VS Code) busca las librerías en tu sistema operativo, pero están instaladas dentro del contenedor de Docker.
 
- **Solución:** Crear un entorno virtual (`python -m venv.venv`) e instalar las librerías ahí (`pip install fastapi pymysql`) para que el IDE tenga autocompletado inteligente. No afecta a la ejecución en Docker.
 

### Error 500: Internal Server Error al hacer un POST

- **Causa:** Hubo un fallo interno en Python. Para ver el error real, hay que consultar los logs del contenedor de la API.
 
- **Comando clave:** `docker logs <nombre-contenedor-api>` (ej: `docker logs 40-api-1`).
 
- **Ejemplo común:** `Unknown column 'titulo' in 'field list'`. Esto ocurre si se creó la tabla manualmente desde Adminer antes de que Python la creara, dejando la estructura incompleta. **Solución:** Borrar la tabla manual desde Adminer y reiniciar el contenedor de la API (`docker compose restart api`) para que la autogenere correctamente.