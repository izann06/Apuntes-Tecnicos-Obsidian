**Tags:** #aws #seguridad #cifrado #kms #macie #acm #cloud-practitioner #cp-seguridad

> [!summary] El Concepto Clave
> Cifrar datos significa convertirlos en texto incomprensible usando una llave matemática (clave criptográfica). Solo quien tenga la misma llave podrá descifrar y leer los datos originales. En AWS, debes proteger los datos en dos estados diferentes: cuando están guardados (En Reposo) y cuando están viajando por internet (En Tránsito).

---

## 🛑 1. Datos en Reposo (Data at Rest)

Son los datos que están inactivos, guardados en un disco duro o en una base de datos. Si un atacante roba el disco duro físico de un centro de datos de AWS, el cifrado en reposo garantiza que solo verá un galimatías de símbolos.

### Integración por defecto en AWS:

* **Amazon S3:** Todo lo que subes a un bucket nuevo hoy en día se cifra por defecto automáticamente.

* **Amazon EBS:** Puedes marcar una casilla para cifrar todo el disco duro virtual de una instancia EC2 (incluido el sistema operativo).

* **Amazon DynamoDB:** Toda la base de datos está cifrada del lado del servidor de forma predeterminada sin que tengas que hacer nada.

### AWS Key Management Service (AWS KMS)

* **¿Qué es?** Es el servicio maestro donde creas y guardas tus "llaves matemáticas" (Claves Criptográficas).

* **El Superpoder:** KMS es como una caja fuerte. Puedes crear la llave para cifrar tus datos de S3 o EBS, pero **tú nunca puedes sacar la llave fuera de KMS**. Cuando S3 necesita cifrar un archivo, llama a KMS para que lo haga. Si sospechas que alguien te está hackeando, puedes desactivar la llave en KMS y *todos tus datos cifrados se volverán instantáneamente ilegibles para todo el mundo* (incluido tú, hasta que la vuelvas a activar).

### Amazon Macie (El Sabueso de S3)

* **¿Qué es?** Un servicio de seguridad impulsado por Machine Learning.

* **¿Qué hace?** Lee tus archivos guardados en Amazon S3 buscando **datos confidenciales que hayas olvidado asegurar** (ej. números de tarjetas de crédito sueltos en un Excel, pasaportes, datos médicos). Si encuentra algo privado expuesto, te envía una alerta de seguridad inmediatamente.

---

## 🚄 2. Datos en Tránsito (Data in Transit)

Son los datos que se están moviendo a través de la red (ej. desde tu servidor de AWS hacia el teléfono móvil de tu cliente).

* **La Amenaza:** Un hacker podría hacer un ataque "Man-in-the-Middle" (ponerse en medio del cable de internet) y leer la tarjeta de crédito de tu cliente mientras viaja.

* **La Solución:** Protocolos **SSL/TLS**. Estos protocolos crean un túnel cifrado entre el cliente y el servidor (es lo que hace que aparezca el "candadito" y el `https://` en tu navegador de internet).

### AWS Certificate Manager (ACM)

* **¿Qué es?** El servicio que genera y administra los certificados SSL/TLS para que tus webs tengan el "candadito verde".

* **El Superpoder:** Los certificados SSL caducan cada año. Antes, un informático tenía que acordarse de renovarlos a mano, y si se le olvidaba, la web dejaba de funcionar. **ACM renueva los certificados automáticamente** de forma gratuita y los despliega en tus balanceadores de carga o en CloudFront sin esfuerzo.

---

## 📊 Chuleta de Emparejamiento

| Si necesitas... | Usa este servicio... |
| :--- | :--- |
| **Crear y guardar las llaves (claves)** para cifrar bases de datos y discos duros. | **AWS KMS (Key Management Service)** |
| Analizar S3 buscando números de tarjetas de crédito filtradas (Machine Learning). | **Amazon Macie** |
| Instalar un "candadito web" (SSL/TLS) para proteger datos mientras viajan (en tránsito). | **AWS Certificate Manager (ACM)** |
| Guardar contraseñas de aplicaciones y rotarlas automáticamente. | **AWS Secrets Manager** (Visto en la lección anterior) |

---

---
→ Volver al índice: [[📂Seguridad/00 - Índice Seguridad|🪐 Seguridad]]
