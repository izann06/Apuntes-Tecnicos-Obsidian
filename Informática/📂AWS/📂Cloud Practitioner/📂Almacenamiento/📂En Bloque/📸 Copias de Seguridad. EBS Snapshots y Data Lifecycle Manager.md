**Tags:** #aws #ebs #snapshots #dlm #backup #cloud-practitioner #cp-almacenamiento

> [!summary] El Concepto Clave
> Tus volúmenes EBS guardan los datos, pero si ocurre un desastre, necesitas una copia de seguridad. Las **Instantáneas (Snapshots)** son "fotografías" de tu disco duro en un momento exacto. Para no volverte loco haciendo estas fotos a mano todos los días, utilizas **Data Lifecycle Manager (DLM)** para que un robot lo haga por ti automáticamente.

---
## 📷 1. Amazon EBS Snapshots (Las Instantáneas)

* **¿Qué son?** Son copias de seguridad puntuales (point-in-time) de tu volumen EBS. Literalmente congelan el estado de tu disco en ese milisegundo exacto y guardan una copia de forma muy segura y redundante en **Amazon S3** (por debajo, AWS hace esto de forma transparente para ti).

* **El Superpoder: Son Incrementales.**
    * Si el Lunes haces una copia de un disco de 100 GB, el snapshot pesa 100 GB.
    * Si el Martes añades 2 GB de datos nuevos y haces otro snapshot, **AWS no vuelve a copiar los 100 GB enteros**. Solo guarda los **2 GB que han cambiado**.
    * *Beneficio:* Esto hace que las copias sean rapidísimas y, sobre todo, que te ahorres muchísimo dinero en costes de almacenamiento.

### 🛠️ Casos de Uso Reales para Snapshots

1. **Recuperación ante desastres:** Si un virus encripta tu servidor, restauras el snapshot de ayer y listo.

2. **Clonación de entornos:** Si tienes tu base de datos de producción y los programadores quieren hacer pruebas sin romper nada, haces un snapshot y creas un volumen EBS nuevo a partir de él. Así les das un entorno de "Pruebas" idéntico al real en cuestión de minutos.

3. **Migración Geográfica:** Los volúmenes EBS están atados a una Zona de Disponibilidad. Si quieres mover tu servidor de París a Tokio, haces un snapshot, lo copias a la región de Tokio, y allí creas un volumen nuevo.

---

## 🤖 2. Amazon Data Lifecycle Manager (DLM)

* **El Problema:** Imagina tener 500 servidores y tener que entrar a la consola de AWS todos los días a las 3:00 AM para pulsar el botón de "Crear Snapshot" en cada uno de ellos. Sería una pérdida de tiempo y, eventualmente, a un humano se le olvidaría hacerlo. Además, si nunca borras los snapshots antiguos, la factura de AWS a fin de mes será gigantesca.

* **La Solución (DLM):** Es un servicio completamente administrado que automatiza la vida útil de tus snapshots.

* **¿Qué hace exactamente?** Tú defines unas **Políticas** y el robot se encarga del resto:
    * *Creación:* "Haz una copia de seguridad todos los días a las 2:00 AM".
    * *Retención / Eliminación:* "Guarda solo las copias de los últimos 30 días. Elimina automáticamente la del día 31 para no pagar almacenamiento de más".

---

## ⚖️ 3. Tu Responsabilidad

Según el modelo de AWS, Amazon se encarga de que la infraestructura donde se guardan los snapshots (S3) no se rompa. Pero **TÚ (El Cliente)** eres responsable de:

1. Programar y administrar cuándo se hacen los snapshots.
2. Borrar los antiguos para no pagar de más.
3. Cifrar (ponerle contraseña) a los snapshots si tienen datos sensibles.
4. Probar de vez en cuando que los snapshots funcionan y se pueden restaurar.

---
→ Volver al índice: [[📂Almacenamiento/00 - Índice Almacenamiento|🪐 Almacenamiento]]
