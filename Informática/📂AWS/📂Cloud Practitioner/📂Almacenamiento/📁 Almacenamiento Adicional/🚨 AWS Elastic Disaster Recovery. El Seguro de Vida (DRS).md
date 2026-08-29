**Tags:** #aws #disaster-recovery #drs #continuidad-negocio #cloud-practitioner #cp-almacenamiento

> [!summary] El Concepto Clave
> Una copia de seguridad (Backup) te devuelve tus archivos perdidos, pero puedes tardar días en comprar un servidor nuevo, instalar Windows y volcar los datos. **Elastic Disaster Recovery** te devuelve *el servidor entero funcionando en minutos* si tu centro de datos principal sufre una catástrofe.

---
## 🏢 La Analogía: El "Restaurante Fantasma"

* **El Método Antiguo:** Para estar seguros, los bancos y hospitales pagaban por tener un segundo centro de datos físico (un "Edificio B") idéntico al "Edificio A", pero apagado. Es como pagar el alquiler de un restaurante entero totalmente equipado y con los ingredientes frescos, solo "por si acaso" se quema tu restaurante principal. Es carísimo.

* **El Método AWS (Elastic Disaster Recovery):** AWS te alquila un trastero muy barato donde guarda un "clon" exacto de tu restaurante (los datos se copian en tiempo real de forma continua). Si ocurre un desastre, AWS coge ese clon, lo "despierta" instalándolo en sus servidores (instancias EC2), y en cuestión de minutos tu negocio vuelve a funcionar desde la nube. **Solo pagas por los servidores caros cuando realmente hay una emergencia o haces un simulacro.**

---

## 🚀 1. Beneficios Principales

* **Resiliencia Empresarial (Recuperación en minutos):** Como la replicación de datos es *continua* (a nivel de bloque de disco), la pérdida de datos es mínima y el tiempo que tardas en volver a estar online (tiempo de inactividad) es cortísimo.

* **Pruebas No Disruptivas:** Puedes hacer "simulacros de incendio" arrancando los servidores clonados en AWS para ver si todo funciona, **sin afectar ni apagar** tus servidores reales de producción.

* **Optimización Masiva de Costes:** Puedes despedirte de tu costoso centro de datos secundario físico. Pides y pagas los recursos completos solo cuando ocurre un desastre.

---

## 🎯 2. Casos de Uso Comunes (Sectores Críticos)

Cualquier empresa que pierda miles de euros por cada minuto que su sistema esté caído es el cliente ideal de este servicio:

1. **Sanidad (Hospitales):** Si el servidor de un hospital cae, los médicos no pueden ver los historiales de los pacientes. Elastic Disaster Recovery permite replicar los sistemas locales en AWS para cumplir normativas estrictas y nunca perder acceso.

2. **Servicios Financieros (Bancos):** El procesamiento de transacciones no puede detenerse nunca. Mantienen la confianza de los clientes y evitan multas millonarias al conmutar rápidamente a la nube si su servidor principal falla.

3. **Fabricación (Fábricas Globales):** Si el sistema que coordina la cadena de montaje se cae, la fábrica se detiene por completo. AWS mantiene un clon de seguridad que asume el control casi al instante en caso de desastre.

---
→ Volver al índice: [[📂Almacenamiento/00 - Índice Almacenamiento|🪐 Almacenamiento]]
