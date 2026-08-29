**Tags:** #aws #regiones #infraestructura-global #compliance #latencia #cloud-practitioner #cp-infraestructura-global
http://googleusercontent.com/image_content/236


> [!warning] El Aislamiento de Datos (Regla de Oro de AWS)
> Cada Región de AWS está **completamente aislada** de las demás. Por defecto, **ningún dato entra o sale de tu entorno** sin que tú otorgues explícitamente el permiso. Esto es vital para la seguridad y el cumplimiento legal.

---

A la hora de expandir tu arquitectura, no eliges una Región al azar. Debes evaluar tus opciones pasando siempre por estos **4 filtros en orden de importancia**:

## ⚖️ 1. Conformidad (Compliance) - *El factor eliminatorio*

Es el factor más crítico. Si las leyes de tu industria te obligan a algo, las demás opciones ya no importan.

* **El concepto:** Los datos están sujetos a las leyes locales del país donde se encuentra la Región.

* **Ejemplos prácticos:** 

 * Si manejas datos de ciudadanos europeos, el **RGPD** te obligará a mantener los datos dentro de la Unión Europea (ej. Región de París o Frankfurt).

 * Si manejas datos financieros en Alemania, las leyes dictan que no pueden salir de allí (Región de Frankfurt).

 * Si operas en China, debes usar obligatoriamente las Regiones ubicadas dentro de sus fronteras.


## ⚡ 2. Proximidad y Latencia

Si no tienes bloqueos legales, tu siguiente prioridad es que tu aplicación vaya rápida.

* **El concepto:** Los datos viajan a través de cables físicos por el mundo. Cuanto más cerca esté el servidor del usuario final, menos tiempo de viaje (menor latencia).

* **Ejemplo práctico:** Si tus clientes están en España, usar las regiones de Zaragoza, París o Milán hará que la web cargue casi al instante. Usar la Región de Australia causaría demoras y una mala experiencia de usuario.

## 🛠️ 3. Disponibilidad de Características (Herramientas)

No todas las Regiones son exactamente iguales por dentro.

* **El concepto:** AWS lanza nuevos servicios constantemente, pero no los despliega en todo el mundo a la vez. Normalmente, las novedades salen primero en EE. UU. (Virginia u Oregón) y luego se van expandiendo.

* **Ejemplo práctico:** Puede que quieras usar un servicio de Inteligencia Artificial muy novedoso, pero descubras que en la Región de España aún no está disponible.

* **Regiones Especiales:** Existen regiones como **AWS GovCloud**, diseñadas *exclusivamente* para el gobierno de EE. UU. con controles de seguridad de personal físico que no existen en las regiones públicas.

## 💰 4. Precios

Ejecutar exactamente el mismo servidor EC2 no cuesta lo mismo en todas las ciudades del mundo.

* **El concepto:** Los costes operativos de Amazon (precio de la electricidad, suelo, impuestos locales) varían de un país a otro. AWS te transfiere esos costes.

* **Ejemplo práctico:** Implementar tu infraestructura en la región de Brasil (São Paulo) suele ser bastante más caro que hacerlo en EE. UU. (Norte de Virginia) debido a los impuestos locales y la infraestructura del país.

---

---

---
→ Volver al índice: [[📂Infraestructura Global/00 - Índice Infraestructura Global|🪐 Infraestructura Global]]
