#github #repositorios #gh-foundations

> [!info] Navegación
> ◀ [[D1 - Introducción a Git y GitHub]] · ▶ [[D3 - Colaboración (Issues, PRs y Discussions)]]

---

# Dominio 2 — Trabajando con Repositorios de GitHub

## 2.1 Anatomía de un Repositorio

Un repositorio bien organizado debe incluir una serie de archivos de documentación estándar que comunican las reglas y propósito del proyecto a los colaboradores.

### El README.md — La Puerta de Entrada

El `README.md` es el primer archivo que ve cualquier persona que visita el repositorio. Un buen README debe incluir:

- **Nombre y descripción** del proyecto.
- **Insignias (Badges):** Estado del build, cobertura de tests, licencia.
- **Instrucciones de instalación** paso a paso.
- **Ejemplos de uso.**
- **Cómo contribuir.**
- **Licencia.**

### Archivos de Repositorio Recomendados

| Archivo | Propósito |
| :--- | :--- |
| `README.md` | Descripción e instrucciones del proyecto |
| `LICENSE` | Define los términos de uso y distribución del código |
| `CONTRIBUTING.md` | Guía para colaboradores: cómo reportar bugs, cómo hacer PRs |
| `CODEOWNERS` | Asigna automáticamente revisores a partes específicas del código |
| `.gitignore` | Lista de archivos/carpetas que Git debe ignorar |
| `CODE_OF_CONDUCT.md` | Normas de convivencia de la comunidad |

> [!tip] El archivo CODEOWNERS
> El archivo `CODEOWNERS` usa una sintaxis similar a `.gitignore` para asignar propietarios:
> ```
> # Todos los archivos .js son revisados por el equipo frontend
> *.js @org/frontend-team
> 
> # La carpeta /docs es revisada por @izanm
> /docs @izanm
> ```
> Cuando alguien abre un PR que modifica esos archivos, GitHub solicita automáticamente la revisión al propietario definido.

---

## 2.2 Navegación y Gestión de Repositorios

### Crear un Repositorio Nuevo

Al crear un repositorio en GitHub puedes configurar:

- **Nombre y descripción.**
- **Visibilidad:** Público (visible para todos) o Privado (solo tú y colaboradores).
- **Inicializar con README** (recomendado).
- **Añadir .gitignore** según el lenguaje del proyecto.
- **Elegir una Licencia** (MIT, Apache 2.0, GPL, etc.).

### Plantillas de Repositorio (Repository Templates)

Un repositorio puede marcarse como **"Template Repository"** en su configuración. Esto permite que otros usuarios generen nuevos repositorios con la misma estructura de archivos, ahorrando tiempo en la configuración inicial.

> [!example] Caso de uso real
> Una empresa crea un repositorio plantilla con la estructura de proyecto, el CI/CD preconfigurado, el `.gitignore`, el `CONTRIBUTING.md` y las Actions. Cada nuevo proyecto parte de ahí con un solo clic.

### Clonar un Repositorio

**Clonar** es descargar una copia completa del repositorio (con todo su historial) a tu máquina local.

```bash
# Clonar via HTTPS (pide usuario/contraseña o token)

git clone https://github.com/usuario/repositorio.git

# Clonar via SSH (requiere clave SSH configurada, recomendado)

git clone git@github.com:usuario/repositorio.git

# Clonar en una carpeta con un nombre específico

git clone <url> nombre-de-carpeta
```

### Crear una Rama Nueva

```bash
# Desde la CLI

git checkout -b nombre-de-rama

# En GitHub Web: botón del selector de rama → "Create new branch"

```

### Añadir Archivos a un Repositorio

```bash
git add nombre-archivo.txt    # Añade un archivo específico al staging area
git add .                      # Añade todos los cambios del directorio actual
git status                     # Ver qué archivos están en staging y cuáles no
git commit -m "mensaje"        # Confirma los cambios con un mensaje
git push origin nombre-rama    # Sube los cambios a GitHub
```

---

## 2.3 Insights y Funciones de Descubrimiento

### Ver Insights del Repositorio

La pestaña **"Insights"** de un repositorio muestra:

- **Pulse:** Resumen de la actividad reciente (PRs, issues, commits).
- **Contributors:** Gráfica de contribuciones por usuario.
- **Traffic:** Visitantes y clonaciones del repositorio.
- **Dependency Graph:** Dependencias del proyecto.
- **Code Frequency:** Adiciones y eliminaciones de líneas por semana.

### Stars (Favoritos)

**Marcar un repositorio con una ⭐ estrella** sirve para:

- Guardarlo como favorito para encontrarlo fácilmente después.
- Mostrar aprecio al autor del proyecto.
- Descubrir proyectos relacionados en "Repositories starred by people you follow".

### Feature Previews

GitHub ofrece **previsualizaciones de características** (Feature Previews) que son funcionalidades en fase beta que puedes activar en tu cuenta antes de su lanzamiento oficial. Se acceden desde `Settings > Feature Preview`.
