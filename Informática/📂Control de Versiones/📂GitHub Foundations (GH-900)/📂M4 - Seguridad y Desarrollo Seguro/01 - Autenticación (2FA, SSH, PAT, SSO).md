#github #gh-foundations #modulo-4 #seguridad #2fa #ssh #pat #sso

> [!info] Navegación
> ◀ [[03 - Equipos, Facturación y Sincronización]] · ▶ [[02 - Dependencias y Dependabot]]

---

# 01 — Autenticación (2FA, SSH, PAT, SSO)

> **Resumen ejecutivo:**
> 1. Las contraseñas HTTPS ya **no funcionan** para Git desde agosto de 2021. Usa SSH o PAT.
> 2. La **2FA** es obligatoria en organizaciones serias. Métodos: App TOTP, Security Key, SMS, GitHub Mobile.
> 3. Los **Fine-grained PATs** son más seguros que los PAT Classic porque limitan permisos por repo.

---

## 1. Métodos de Autenticación

> [!WARNING] Contraseñas HTTPS eliminadas
> Desde agosto de 2021, GitHub **eliminó la autenticación por contraseña** para operaciones Git por HTTPS. Ya no puedes hacer `git push` introduciendo tu contraseña. Debes usar un **Personal Access Token (PAT)** o una **clave SSH**.

### Tabla Resumen de Métodos

| Método | ¿Para qué sirve? | Seguridad |
| :--- | :--- | :---: |
| **SSH Keys** | Autenticarte para `git push/pull` sin contraseña | ⭐⭐⭐⭐⭐ |
| **PAT (Fine-grained)** | Token con permisos granulares por repo y caducidad | ⭐⭐⭐⭐ |
| **PAT (Classic)** | Token con alcance amplio a toda la cuenta | ⭐⭐⭐ |
| **SAML SSO** | Login único corporativo (Enterprise) | ⭐⭐⭐⭐⭐ |
| **OAuth Apps** | Autorizar apps de terceros a acceder a tu cuenta | ⭐⭐⭐ |

---

## 2. Autenticación de Doble Factor (2FA)

La **2FA** añade una segunda capa de seguridad. Aunque alguien robe tu contraseña, necesitará el segundo factor para acceder.

| Método 2FA | Descripción | Nivel de seguridad |
| :--- | :--- | :---: |
| **Security Key (Hardware)** | Llaves físicas como YubiKey. | ⭐⭐⭐⭐⭐ Máximo |
| **Authenticator App (TOTP)** | Apps como Google Authenticator, Authy. Código de 6 dígitos cada 30s. | ⭐⭐⭐⭐ **Recomendado** |
| **GitHub Mobile** | Aprueba el acceso desde la app del móvil. | ⭐⭐⭐⭐ |
| **SMS** | Código por mensaje de texto. | ⭐⭐ Vulnerable a SIM swapping |

> [!IMPORTANT] 2FA obligatorio
> GitHub está exigiendo 2FA a los contribuidores activos. Las organizaciones pueden **forzar 2FA** a nivel de organización: cualquier miembro que no lo tenga activado es automáticamente removido. Esto sale en el examen.

---

## 3. Claves SSH

Las claves SSH permiten autenticarte sin contraseña ni tokens. Se basan en un par de claves criptográficas:

- **Clave privada:** Se queda en tu máquina. NUNCA se comparte.
- **Clave pública:** Se sube a GitHub (`Settings > SSH and GPG keys`).

```bash
# Generar un par de claves SSH (Ed25519, recomendado)
ssh-keygen -t ed25519 -C "izan@email.com"

# Salida esperada:
# Generating public/private ed25519 key pair.
# Enter file in which to save the key (/home/izan/.ssh/id_ed25519):
# Enter passphrase (empty for no passphrase):
# Your public key has been saved in /home/izan/.ssh/id_ed25519.pub
```

```bash
# Añadir la clave al agente SSH
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Copiar la clave pública para pegarla en GitHub
cat ~/.ssh/id_ed25519.pub
# Salida: ssh-ed25519 AAAAC3Nza... izan@email.com
```

```bash
# Verificar la conexión
ssh -T git@github.com

# Salida esperada:
# Hi izanm! You've successfully authenticated, but GitHub does not provide shell access.
```

---

## 4. Personal Access Tokens (PAT)

### PAT Classic vs. Fine-grained

| Característica | PAT Classic | Fine-grained PAT |
| :--- | :--- | :--- |
| **Alcance (Scope)** | Amplio: se define a nivel de cuenta completa | Granular: se define por repositorio y permiso |
| **Caducidad** | Opcional (puede no caducar) | **Obligatoria** (debes poner fecha de expiración) |
| **Permisos** | Checkboxes amplios (repo, workflow, admin) | Permisos específicos (read contents, write issues) |
| **Recomendado** | ❌ Solo si el Fine-grained no es compatible | ✅ Siempre que sea posible |

> [!WARNING] Pregunta frecuente de examen
> Si el examen pregunta cuál es el tipo de PAT **más seguro**, la respuesta es **Fine-grained**. Porque fuerza una caducidad y permite permisos solo en los repos que elijas, siguiendo el principio de mínimo privilegio.

---

## 5. SAML SSO y OAuth

### SAML Single Sign-On (SSO)

Disponible en **GitHub Enterprise Cloud**. Permite que los empleados se autentiquen en GitHub usando las credenciales de su empresa (Azure AD, Okta, etc.).

- Los usuarios inician sesión una sola vez en el IdP corporativo y acceden a GitHub sin credenciales adicionales.
- La organización puede forzar que **todos los miembros pasen por el SSO**.

### OAuth Apps

Permiten que aplicaciones de terceros accedan a tu cuenta de GitHub con los permisos que tú autorices. Ejemplo: un servicio de CI/CD que necesita leer tus repositorios.
