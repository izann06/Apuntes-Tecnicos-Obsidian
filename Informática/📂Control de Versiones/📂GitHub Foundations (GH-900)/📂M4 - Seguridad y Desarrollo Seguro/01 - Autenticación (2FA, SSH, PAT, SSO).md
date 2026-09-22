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
> Desde agosto de 2021, GitHub **eliminó la autenticación por contraseña** para operaciones Git por HTTPS. Ya no puedes hacer `git push` tecleando tu contraseña de GitHub. Debes usar un **Personal Access Token (PAT)** o una **clave SSH**.

**¿Por qué has estado usando Git sin darte cuenta de esto?**

Seguramente pienses: *"Pero si yo he estado haciendo `git push` sin configurar nada de esto"*. Eso es porque en Windows/Mac existe un programa secundario llamado **Git Credential Manager** (o si usas GitHub Desktop). Cuando inicias sesión la primera vez, se abre una ventana del navegador; ahí autorizas a GitHub, se genera un token por detrás automáticamente y se guarda en tu ordenador para que no te lo vuelva a pedir. Pero bajo el capó, Git **nunca** está enviando tu contraseña, está usando tokens.

### Ejemplo práctico: HTTPS vs SSH a la hora de clonar

Cuando vas a clonar un repositorio, GitHub te da dos enlaces. Dependiendo de cuál elijas, el proceso cambia:

1. **Clonar por HTTPS (`https://github.com/usuario/repo.git`)**

   * **¿Qué pasa al hacer push?** Si no usas Git Credential Manager, la terminal te pedirá un `Username` y un `Password`.
   
   * **El truco:** Donde dice "Password", NO puedes poner la contraseña de tu cuenta. Tienes que ir a GitHub, generar un **PAT (Personal Access Token)**, que es una cadena larguísima (ej: `ghp_1234abcd...`), copiarlo y pegarlo ahí.

2. **Clonar por SSH (`git@github.com:usuario/repo.git`)**

   * **¿Qué pasa al hacer push?** No te pide NADA. Git simplemente empuja el código directo.
   
   * **¿Por qué usamos SSH?** Porque es mucho más cómodo para los programadores. En lugar de estar generando y copiando tokens que caducan (PATs), generas una **Clave SSH** en tu ordenador una sola vez en la vida, se la subes a GitHub, y a partir de ahí tu ordenador y GitHub se reconocen automáticamente por criptografía pura.

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
> GitHub está exigiendo 2FA a los contribuidores activos. Las organizaciones pueden **forzar 2FA** a nivel de organización: cualquier miembro que no lo tenga activado es automáticamente removido. Esto sale en el examen

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

¿Has visto alguna vez el botón **"Iniciar sesión con Microsoft"** o **"Iniciar sesión con Google"** en la web del trabajo? Eso es SSO (Single Sign-On).

En empresas grandes (GitHub Enterprise Cloud), los administradores no quieren que los programadores tengan contraseñas separadas para el correo, para el chat y para GitHub. 
* Con **SAML SSO**, la empresa conecta su directorio central (IdP) con GitHub.
* Cuando el programador intenta entrar a la organización en GitHub, este le redirige a la web corporativa de Microsoft/Okta. Allí pone el correo y contraseña del trabajo, y vuelve a GitHub autenticado.

* **Ventaja:** Si despiden a la persona y le cortan el correo corporativo, automáticamente pierde el acceso a GitHub. Además, la empresa puede forzar que **nadie** acceda a los repositorios de la organización si no es usando este sistema corporativo.

### OAuth Apps (Aplicaciones de terceros)

Imagina que estás usando un servicio externo como **Vercel** o **Netlify** para alojar tu página web, y te dicen: *"Oye, necesito acceso a tu código de GitHub para poder publicarlo por ti"*.

Obviamente **no le vas a dar tu usuario y contraseña** de GitHub a Vercel. 

Ahí entra **OAuth**. Es un sistema donde:

1. Haces clic en "Conectar con GitHub".
2. GitHub te saca una pantalla diciendo: *"Vercel quiere leer tus repositorios, ¿le dejas?"*.
3. Si le das a aceptar, GitHub le da a Vercel un "pase VIP" (un token de OAuth) que solo sirve para leer repositorios.
4. Si un día dejas de usar Vercel, vas a `Settings > Applications > Authorized OAuth Apps` en GitHub y le revocas el pase VIP. Tu contraseña original de GitHub nunca estuvo en peligro.
