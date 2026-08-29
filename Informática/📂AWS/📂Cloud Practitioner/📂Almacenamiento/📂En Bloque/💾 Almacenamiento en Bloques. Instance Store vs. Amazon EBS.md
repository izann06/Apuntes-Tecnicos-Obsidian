**Tags:** #aws #ec2 #ebs #instance-store #almacenamiento #cloud-practitioner #cp-almacenamiento

> [!summary] El Concepto Clave
> El almacenamiento a nivel de bloque es básicamente un disco duro. La gran diferencia en AWS radica en **dónde está conectado** ese disco duro y **qué pasa con tus datos** si apagas el servidor.

---

## 📝 1. Almacén de Instancias EC2 (Instance Store) - "La Libreta del Camarero"

* **¿Qué es?** Es un disco duro que está **conectado físicamente** al mismo ordenador (hardware host) donde se está ejecutando tu máquina virtual EC2.

* **La Analogía:** Es como la pequeña libreta de papel que el camarero lleva en el bolsillo. Es rapidísimo escribir en ella porque la tiene en la mano.

* **El Problema (Lo Efímero):** Si detienes (apagas) la instancia EC2, AWS mueve tu máquina virtual a otro ordenador físico para optimizar recursos. Como el disco duro físico se quedó en el ordenador anterior, **TODOS TUS DATOS SE BORRAN PARA SIEMPRE**.

* **Beneficios:** Viene incluido gratis con muchos tipos de instancias y ofrece un rendimiento/velocidad (I/O) extremo porque no viaja por cables de red.

* **Casos de Uso:** Información que no te importa perder. Archivos temporales, memoria caché, búferes, o datos que se pueden volver a calcular fácilmente.

---

## 🗄️ 2. Amazon Elastic Block Store (Amazon EBS) - "La Caja Registradora Central"

* **¿Qué es?** Es un disco duro virtual (volumen) que se conecta a tu instancia EC2 **a través de la red** interna de AWS. No está físicamente soldado al ordenador de tu servidor.

* **La Analogía:** Es como el sistema informático de la caja registradora del restaurante. Si el camarero (la instancia EC2) termina su turno y se va a casa (se detiene la instancia), los datos de las ventas siguen intactos en el sistema.

* **El Superpoder (La Persistencia):** Si detienes tu instancia EC2 o incluso si la destruyes (terminas), el volumen EBS **sobrevive** de forma independiente. Tus datos persisten.

* **Beneficios:** * **Persistencia:** No pierdes datos al apagar.

 * **Portabilidad:** Puedes desconectar un volumen EBS de un servidor y conectárselo a otro diferente en segundos.

 * **Copias de Seguridad:** Permite hacer "fotografías" exactas del disco (Snapshots) para guardar copias de seguridad.

* **Casos de Uso:** Bases de datos, sistemas de archivos del sistema operativo, software empresarial, y cualquier dato crítico que necesites conservar a largo plazo.

---

## 📊 ¿Cuál elegir?

| Característica | Instance Store (Almacén de Instancias) | Amazon EBS |
| :--- | :--- | :--- |
| **Persistencia de datos** | ❌ Se pierden al detener la instancia. | ✅ Sobreviven al detener la instancia. |
| **Conexión** | Físicamente en el hardware anfitrión. | A través de la red de AWS. |
| **Rendimiento** | Altísimo (Ideal para cachés rápidos). | Alto (Depende del tipo de volumen que pagues). |
| **Independencia** | Muere con la instancia. | Existe independientemente de la instancia. |

---
→ Volver al índice: [[📂Almacenamiento/00 - Índice Almacenamiento|🪐 Almacenamiento]]
