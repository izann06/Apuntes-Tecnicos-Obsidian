**Tags:** #gobernanza #cumplimiento #audit-manager #artifact #config #ia #m5-seguridad

> [!quote] Contexto
> La Gobernanza en IA no es solo proteger los datos de los hackers (Seguridad), sino garantizar el **cumplimiento normativo**, trazar el uso de los datos y tener políticas organizativas claras. El examen hace mucho hincapié en qué herramienta usar para qué auditoría.

---

## 🏛️ Cheat Sheet: Servicios de Cumplimiento de AWS

Para el examen, empareja directamente el caso de uso con el servicio:

| Servicio AWS | Cuándo usarlo (Palabra clave del examen) |
| :--- | :--- |
| **AWS Config** | Monitoreo y detección de **cambios de configuración** no autorizados. (Ej: "Alguien abrió el puerto 22 o hizo público un S3 bucket de entrenamiento"). |
| **Amazon Inspector** | Detección automática de **vulnerabilidades** de software en el código y en dependencias del sistema operativo. |
| **AWS Audit Manager** | Recolección **continua** de evidencia de **cumplimiento normativo** (GDPR, HIPAA, ISO). Traduce políticas en la nube a evidencia para auditores externos. |
| **AWS Artifact** | Repositorio central estático de **informes oficiales** y certificaciones de seguridad de AWS (ej. el certificado SOC2 de AWS). |
| **AWS CloudTrail** | Log unificado de **todas las acciones de API** en la cuenta (Quién hizo qué y cuándo). |
| **AWS Trusted Advisor** | Recomendaciones automáticas sobre las mejores prácticas de AWS (**Seguridad, Costes, Límites de cuota, Rendimiento, Tolerancia a fallos**). |

> [!warning] Trampa Clásica de Examen
> Si te preguntan "Dónde descargo la prueba de que el datacenter de AWS cumple con la normativa HIPAA" ➔ **AWS Artifact** (Documentos de AWS).
> Si te preguntan "Cómo genero evidencia de que MI infraestructura de IA cumple con HIPAA" ➔ **AWS Audit Manager** (Tu cumplimiento continuo).

---

## 📊 Estrategias de Gobernanza de Datos en IA

Cuando manejas Terabytes de datos para entrenar modelos o alimentar un sistema RAG, la organización de los datos es vital:

### 1. Ciclo de Vida (Amazon S3 Lifecycle Policies)
Mantener todos los datos eternamente es carísimo e incumple leyes de retención.

- **La solución:** Políticas de S3 que mueven datos antiguos de forma automática a S3 Glacier (archivo barato) o los borran permanentemente cuando superan los 5 años (cumplimiento legal).

### 2. Data Lineage (Trazabilidad del Dato)
> [!abstract] La Trazabilidad Alimentaria
> Al igual que necesitas saber de qué granja viene un trozo de carne contaminado, necesitas saber exactamente qué archivo PDF entrenó a tu modelo o generó una respuesta sesgada.

- SageMaker provee capacidades de **ML Lineage Tracking** para conectar cada modelo desplegado con la versión exacta de los datos que lo entrenó.

### 3. Residencia de Datos (Data Residency)
Las leyes nacionales (como el GDPR en Europa) obligan a que los datos de los ciudadanos europeos no salgan de las fronteras europeas.

- **La solución en AWS:** Como cliente, tú eliges la Región de AWS (ej. `eu-west-1` Irlanda). AWS **garantiza** que los datos nunca se moverán a otra región (ej. `us-east-1` USA) sin tu permiso explícito. Bedrock procesará los prompts localmente en esa región.

---

## 📐 Marcos Organizativos para IA Generativa

Antes de desplegar cualquier aplicación de IA Generativa, una empresa debe clasificar su nivel de riesgo. AWS sugiere utilizar marcos de trabajo estructurados:

### Generative AI Security Scoping Matrix
Es una matriz que cruza diferentes factores para clasificar el riesgo de la aplicación (Bajo, Medio, Alto, Crítico) y definir qué nivel de supervisión necesita:

1. **Sensibilidad de los Datos:** ¿Usa datos públicos, corporativos internos, o altamente clasificados (PHI/PII)?

2. **Impacto en el Usuario:** ¿Afecta a la salud, finanzas o libertad de un humano?

3. **Nivel de Personalización:** ¿Usas el modelo tal cual (bajo riesgo), usas RAG (riesgo medio), o haces Fine-Tuning con datos propios (riesgo alto)?

### Cadencia de Revisión
Los modelos fundacionales se degradan con el tiempo a medida que el mundo cambia (Data Drift). La gobernanza requiere establecer una cadencia rígida y programada de:

- Escaneo de vulnerabilidades.

- Monitorización del modelo (Amazon SageMaker Model Monitor).

- Re-entrenamiento con datos actualizados.

---
→ Volver al índice: [[📂M5 - IA Responsable y Seguridad/00 - Índice Módulo 5|🪐 Módulo 5: IA Responsable y Seguridad]]
