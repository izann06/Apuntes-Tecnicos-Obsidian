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

# 3.Configuración de Claves SSH en GitHub

Las claves SSH permiten autenticarte en GitHub sin tener que escribir contraseñas ni generar tokens personales constantemente. Funcionan mediante un par criptográfico:

  

- **Clave privada (`id_ed25519`):** Reside únicamente en tu máquina local. **Nunca se comparte**.  
    
- **Clave pública (`id_ed25519.pub`):** Se añade a tu cuenta de GitHub (**Settings > SSH and GPG keys**).

### Paso 1: Generar el par de claves

Abre la terminal (Git Bash o terminal Unix) y navega al directorio `.ssh`:

```Bash
cd ~/.ssh
```

Genera un nuevo par de claves usando el algoritmo Ed25519:

```Bash
ssh-keygen -t ed25519 -C "tu-email@ejemplo.com"
```

**Salida y respuestas interactivas:**

```Plaintext
Generating public/private ed25519 key pair.
Enter file in which to save the key

(/c/Users/usuario/.ssh/id_ed25519):nombre-clave-de-ssh
o Presiona Enter para nombre por defecto

Enter passphrase (empty for no passphrase): [Opcional: introduce una frase de paso o pulsa Enter]
Enter same passphrase again: [Pulsa Enter]
Your identification has been saved in /c/Users/usuario/.ssh/id_ed25519
Your public key has been saved in /c/Users/usuario/.ssh/id_ed25519.pub
```

### Paso 2: Iniciar y cargar la clave en el Agente SSH

Inicia el proceso del agente SSH en segundo plano:

```Bash
eval "$(ssh-agent -s)"
```

Añade tu clave privada al agente:

```Bash
ssh-add id_ed25519
```

### Paso 3: Configurar el archivo SSH (`~/.ssh/config`)

Crea o edita el archivo de configuración para que Git use la clave correcta automáticamente:

Si no has creado el archivo **config**
```Bash
touch config
```

Entra en él
```Bash
nano ~/.ssh/config
```

Pega la configuración correspondiente a tu sistema operativo:

- **En Windows (Git Bash) / Linux:**
    
```Fragmento de código
    Host github.com
      AddKeysToAgent yes
      IdentityFile ~/.ssh/id_ed25519 -> Nombre que le pusiste a la clave de ssh. 
```

Guarda los cambios con Ctrl + O y Enter y sal del editor Ctrl + X.


### Paso 4: Añadir la clave pública a GitHub

1. Imprime y copia el contenido completo de tu clave pública:
    
```Bash
cat id_ed25519.pub
```
    
2. En tu navegador, ve a [GitHub.com](https://github.com/?utm_source=gemini) > Foto de perfil > **Settings**.
    
3. En la barra lateral, haz clic en **SSH and GPG keys**.  
    
4. Haz clic en **New SSH key**.
    
5. Rellena los datos:
    
- **Title:** Nombre identificativo de tu equipo (ej. _Portátil Personal_).
        
- **Key type:** _Authentication Key_.
    
- **Key:** Pega la clave pública copiada.
        
2. Pulsa **Add SSH key**.

### Paso 5: Verificar la conexión

Ejecuta el comando de comprobación:

```Bash
ssh -T git@github.com
```

_Si es la primera vez que conectas, confirma la autenticidad del host escribiendo `yes`._


**Salida esperada:**

```Plaintext
Hi tu-usuario! You've successfully authenticated, but GitHub does not provide shell access.
```

### Paso 6: Usar SSH en tus repositorios (Cambiar de HTTPS a SSH)

Tener la clave configurada en tu ordenador no hace magia por sí sola. Ahora tienes que decirle a tus repositorios locales que dejen de usar HTTPS y empiecen a usar tu nueva clave SSH para hablar con GitHub.

**1. Ver qué protocolo estás usando ahora mismo:**
Ve a la carpeta de tu proyecto local en la terminal y ejecuta:

```bash
git remote -v
```

*Si la salida empieza por `https://...`, tu repositorio local sigue usando el sistema viejo.*

**2. Cambiar el repositorio a SSH:**
Ve a la página de tu repositorio en GitHub, dale al botón verde **Code**, selecciona la pestaña **SSH** y copia la URL (que siempre tiene el formato `git@github.com:usuario/repo.git`). 

Luego, en tu terminal ejecuta:
```bash
git remote set-url origin git@github.com:tu-usuario/tu-repo.git
```

**3. Comprobar que ha funcionado:**
Vuelve a ejecutar `git remote -v`. Si la URL ahora empieza por `git@github.com`, ya lo tienes. ¡A partir de este momento, puedes hacer todos los `git push` y `git pull` que quieras y Git nunca más te pedirá una contraseña o un token!

**EJEMPLO:**

![[01 - Autenticación (2FA, SSH, PAT, SSO).png]]

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
