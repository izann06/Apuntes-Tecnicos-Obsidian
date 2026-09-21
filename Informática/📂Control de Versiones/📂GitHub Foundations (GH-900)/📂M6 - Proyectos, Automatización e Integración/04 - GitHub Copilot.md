#github #gh-foundations #modulo-6 #copilot #ia

> [!info] Navegación
> ◀ [[03 - GitHub Pages y Codespaces]] · ▶ [[🎓 Índice Maestro - GitHub Foundations]]

---

# 04 — Inteligencia Artificial con GitHub Copilot

> **Resumen ejecutivo:**
> 1. **GitHub Copilot** es un programador de pares impulsado por IA (basado en los modelos de OpenAI).
> 2. Existen 3 planes: **Individual** (básico), **Business** (empresas) y **Enterprise** (contexto corporativo profundo).
> 3. Funciona directamente en los principales IDEs y permite autocompletado, chat y generación de pruebas.

---

## 1. Capacidades y Modelos de Planes

GitHub Copilot no es un único producto, sino una suite de funcionalidades potenciadas por inteligencia artificial que se adaptan a diferentes escalas.

| Característica | Copilot Individual | Copilot Business | Copilot Enterprise |
| :--- | :--- | :--- | :--- |
| **Público objetivo** | Desarrolladores solitarios y estudiantes | Equipos y empresas estándar | Grandes corporaciones |
| **Autocompletado de código** | ✅ | ✅ | ✅ |
| **Copilot Chat en el IDE** | ✅ | ✅ | ✅ |
| **Privacidad de datos** | Tú eliges si compartes tus snippets | 🔒 Tus datos NO se usan para entrenar modelos | 🔒 Tus datos NO se usan |
| **Gestión de licencias** | ❌ | ✅ Asignación centralizada por equipos | ✅ Asignación centralizada |
| **Copilot en github.com** | ❌ | ❌ | ✅ Chat directamente en la web |
| **Contexto profundo del repo** | ❌ | ❌ | ✅ Puede responder basándose en el código privado de toda la empresa |
| **Resúmenes automáticos de PRs** | ❌ | ❌ | ✅ Genera descripciones de Pull Requests |

> [!TIP] Gratis para estudiantes
> Si tienes el **GitHub Student Developer Pack** (asociado a un correo `.edu` o universitario verificado), GitHub Copilot Individual es 100% gratuito mientras seas estudiante.

---

## 2. Configuración e Instalación en IDEs

Copilot funciona como una **extensión** instalable en los entornos de desarrollo más populares. No es un programa independiente.

**IDEs y Editores soportados oficialmente:**
- Visual Studio Code
- Visual Studio
- JetBrains (IntelliJ, WebStorm, PyCharm, etc.)
- Neovim
- GitHub Codespaces (suele venir preinstalado)

### Pasos de Configuración Básica
1. Instalar la extensión "GitHub Copilot" y "GitHub Copilot Chat" desde el marketplace del IDE.
2. Iniciar sesión con la cuenta de GitHub que tiene la licencia activa.
3. Autorizar el acceso en el navegador.

---

## 3. Interacción y Atajos de Teclado (Shortcuts)

Copilot interactúa contigo de tres maneras principales:

### 1. Autocompletado Ghost Text
Mientras escribes, Copilot sugiere código en texto grisáceo.
- **Aceptar sugerencia completa:** `Tab`
- **Aceptar palabra por palabra:** `Ctrl + Right Arrow` (Windows/Linux) o `Cmd + Right Arrow` (Mac).
- **Descartar sugerencia:** `Esc`

### 2. Panel de Sugerencias Múltiples
Si la primera sugerencia no te gusta, puedes pedirle a Copilot que genere hasta 10 opciones alternativas en un panel lateral.
- **Abrir panel de sugerencias:** `Ctrl + Enter`

### 3. Interacción por Comentarios (Prompting)
Copilot lee el contexto del archivo, especialmente los comentarios y el nombre de la función. Para pedir algo específico, simplemente descríbelo en un comentario.

```javascript
// Obtener todos los usuarios de la base de datos que sean administradores
// y tengan más de 18 años. Ordenarlos por fecha de creación descendente.
function getAdultAdmins() {
    // ⬇️ Copilot generará el código aquí al pulsar Enter
}
```

> [!WARNING] Pregunta frecuente de examen
> El examen puede preguntar cómo se pueden ver **múltiples sugerencias** de Copilot a la vez si la sugerencia inline no es la adecuada. La respuesta clave es el atajo **`Ctrl + Enter`** (o abrir el panel de Copilot).
