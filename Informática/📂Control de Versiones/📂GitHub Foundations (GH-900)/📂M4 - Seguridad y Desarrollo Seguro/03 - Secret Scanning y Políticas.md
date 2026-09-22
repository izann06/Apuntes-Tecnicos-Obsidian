#github #gh-foundations #modulo-4 #secret-scanning #security-md #bfg

> [!info] Navegación
> ◀ [[02 - Dependencias y Dependabot]] · ▶ [[01 - Repositorios y Documentación]]

---

# 03 — Secret Scanning y Políticas de Seguridad

> **Resumen ejecutivo:**
> 1. **Secret Scanning** detecta credenciales (API keys, tokens) expuestas accidentalmente en commits.
> 2. El archivo `SECURITY.md` define cómo reportar vulnerabilidades de forma responsable.
> 3. Si expones un secreto, debes **rotarlo inmediatamente** y después purgar el historial con BFG o `git filter-repo`.

---

## 1. Secret Scanning

**Secret Scanning** escanea automáticamente el código de tus repositorios en busca de secretos expuestos accidentalmente: API keys, tokens de acceso, contraseñas, claves privadas, etc.

### Funcionamiento

| Tipo                | Descripción                                                                                           | Disponibilidad                                     |
| :------------------ | :---------------------------------------------------------------------------------------------------- | :------------------------------------------------- |
| **Push Protection** | **Bloquea el push** antes de que el secreto llegue al repositorio.                                    | Repos públicos (gratis) + GitHub Advanced Security |
| **Alert Scanning**  | Escanea commits ya subidos y genera alertas si encuentra secretos.                                    | Repos públicos (gratis) + GitHub Advanced Security |
| **Partner Alerts**  | Si detecta un token de un partner (AWS, Azure, Stripe...), notifica al proveedor para que lo revoque. | Repos públicos (automático)                        |
|                     |                                                                                                       |                                                    |

### ¿Qué detecta?

GitHub tiene patrones para detectar secretos de más de 100 proveedores:

- **AWS:** Access Keys (`AKIA...`)
- **Azure:** Tokens de servicio
- **GitHub:** Personal Access Tokens
- **Stripe:** API Keys (`sk_live_...`)
- **Google Cloud:** Service Account Keys
- **Slack:** Webhooks y tokens de bot

> [!WARNING] Push Protection es tu mejor amigo
> Con Push Protection activado, si intentas hacer `git push` con un token de AWS en el código, GitHub **rechaza el push** y te muestra un mensaje de error. Esto previene la exposición antes de que ocurra. Actívalo en `Settings > Code security > Push protection`.

![[03 - Secret Scanning y Políticas.png]]
---

## 2. Política de Seguridad (`SECURITY.md`)

Imagina que alguien encuentra un fallo de seguridad gravísimo en el código de tu empresa. Lo peor que podría hacer esa persona es ir a la pestaña "Issues" de GitHub y crear un reporte público diciendo: *"Oye, he descubierto cómo hackearos haciendo X"*. ¡Si hace eso, todos los hackers del mundo lo leerán y atacarán tu aplicación antes de que tengas tiempo a arreglarlo!

Para evitar esto existe el archivo **`SECURITY.md`**. 

* **¿Qué se pone ahí?** Son simplemente las **instrucciones** de cómo quieres que te contacten "en secreto" si alguien encuentra un fallo. Lo normal es escribir algo como: *"Si encuentras una vulnerabilidad, por favor NO abras un issue público. Envíanos un correo directamente a `seguridad@miempresa.com`"*. También se suele indicar qué versiones de tu código están mantenidas y cuáles ya están obsoletas.

* **¿Dónde aparece en GitHub?** Si creas este archivo en la raíz de tu repositorio (o en la carpeta `.github/`), GitHub lo detecta mágicamente. Si vas a la pestaña **Security** del repositorio, verás un apartado llamado **Security policy** donde se mostrará este texto. Además, GitHub pondrá un aviso automático recordando que lean esto cada vez que alguien intente abrir un nuevo Issue normal.

**Ejemplo de cómo se ve el archivo por dentro:**

```markdown
# Security Policy (Política de Seguridad)

## Versiones soportadas
Actualmente solo lanzamos parches de seguridad para las siguientes versiones:
| Version | Soportada |
| ------- | --------- |
| 2.x.x   | ✅ Sí |
| 1.x.x   | ❌ No (Obsoleta) |

## Cómo reportar una vulnerabilidad
Si descubres un problema de seguridad, por favor envíanos un correo a `security@miempresa.com`. NO abras un Issue público. Responderemos a tu correo en menos de 48 horas.
```

> [!TIP] Exam Tip
> El examen suele preguntar cómo le indicas a la comunidad la forma correcta de reportar vulnerabilidades en tu proyecto. La respuesta es creando un archivo `SECURITY.md`.

---

## 3. Remediación de Credenciales Expuestas

Si ya has subido un secreto a GitHub, sigue este protocolo **inmediatamente**:

### Paso 1: Rotar el secreto (URGENTE)

```
1. Ve al panel del proveedor (AWS Console, Stripe Dashboard, etc.)
2. Revoca / invalida la credencial expuesta
3. Genera una credencial nueva
4. Actualiza tu aplicación con la nueva credencial
```

> [!IMPORTANT] La rotación es lo primero
> Purgar el historial de Git NO es suficiente. Los bots que rastrean GitHub buscan secretos en tiempo real. Si tu API key de AWS estuvo expuesta 5 minutos, **ya puede haber sido robada**. Rota primero, purga después.

### Paso 2: Purgar el historial de Git

Borrar el secreto en un commit nuevo **no lo elimina del historial**. Hay que purgar los commits antiguos:

| Herramienta | Descripción | Complejidad |
| :--- | :--- | :---: |
| **BFG Repo-Cleaner** | Herramienta especializada en limpiar secretos del historial. Rápida y sencilla. | ⭐ Fácil |
| **`git filter-repo`** | Reescritura avanzada del historial. Más flexible pero más compleja. | ⭐⭐⭐ Avanzado |

```bash
# Ejemplo con BFG: eliminar un archivo que contenía secretos
java -jar bfg.jar --delete-files credentials.json
git reflog expire --expire=now --all
git gc --prune=now --aggressive
git push --force
```

> [!WARNING] `git push --force` es necesario
> Después de purgar el historial, debes hacer un force push para sobrescribir el historial remoto en GitHub. Esto **rompe el historial** para cualquier colaborador que ya haya clonado el repo (tendrán que volver a clonar).
