#domotica #home-assistant #iot #smart-home

> [!info] Navegación
> ▶ Siguiente: [[02 - Protocolos (Zigbee, Wi-Fi, Matter)]] (Próximamente)

---

# 01 — Introducción a la Domótica: Home Assistant vs Ecosistemas Cerrados

> **Resumen ejecutivo:**
> 1. La domótica busca automatizar rutinas del hogar. Existen dos enfoques: usar la **nube del fabricante** (fácil, cerrado) o **Home Assistant** (control total, local, multiprotocolo).
> 2. Un **sensor mmWave** detecta presencia (incluso respiración o estando quieto), a diferencia de un sensor PIR clásico que solo detecta movimiento evidente.
> 3. Montar tu propio Home Assistant requiere hardware local (Raspberry Pi o Mini PC) siempre encendido, pero te independiza de internet y de marcas específicas.

---

## 1. El Dilema Inicial: ¿Cómo quiero automatizar?

Imagina que tu objetivo es simple: *"Quiero entrar en mi habitación y que la luz se encienda sola, y se apague cuando no estoy"*. 

Tienes dos caminos para lograrlo:

### Opción A: Ecosistema de Fabricante (Tapo, Aqara, Hue)

Compras todo de la misma marca y usas su aplicación oficial. La bombilla y el sensor se conectan a los servidores de esa marca en internet (la nube), y la app ejecuta la regla.

```mermaid
graph LR
    S[Sensor Tapo] -- WiFi --> N((Nube Tapo / Internet))
    N -- WiFi --> B[Bombilla Tapo]
```

| ✅ Ventajas | ❌ Desventajas |
| :--- | :--- |
| Instalación en 5 minutos (Plug & Play). | **Dependencia de la nube:** Si te quedas sin internet, la luz no se enciende. |
| No requiere hardware adicional (solo el móvil). | **Walled Garden:** Estás atado a comprar siempre dispositivos de esa marca. |
| Inversión inicial mínima. | Es muy difícil (o imposible) mezclar marcas (ej. sensor Aqara encendiendo una luz Tapo). |

### Opción B: Home Assistant (El cerebro local)

Instalas un pequeño ordenador en tu casa que funciona como un "traductor universal". No dependes de la nube; todo ocurre dentro de tu propia red local.

```mermaid
graph LR
    S[Cualquier Sensor] -- Zigbee/WiFi --> HA[[Home Assistant<br>(Mini PC/Raspberry)]]
    HA -- Zigbee/WiFi --> B[Cualquier Bombilla]
```

| ✅ Ventajas | ❌ Desventajas |
| :--- | :--- |
| **Independencia:** Funciona sin internet. Todo es local y privado. | Mayor coste inicial (necesitas comprar el Mini PC/Raspberry). |
| **Traductor universal:** Puedes mezclar un sensor Aqara, un enchufe Sonoff, una luz de IKEA y pedirle a Alexa que lo controle. | Curva de aprendizaje más alta (requiere configuración y mantenimiento). |
| Automatizaciones extremadamente complejas. | Tienes un equipo encendido 24/7. |

> [!TIP] ¿Qué elegir?
> - **Para 1 o 2 habitaciones simples:** Ve por la Opción A (Tapo o Xiaomi).
> - **Si quieres aprender redes, domótica seria y mezclar marcas libremente:** Lánzate a por Home Assistant.

---

## 2. Arquitectura de Home Assistant (El Hardware)

Si te decides por Home Assistant, este es el hardware que necesitas comprar. 

### 1. El Cerebro (El Servidor)

Necesitas un ordenador encendido 24/7 que ejecute el sistema operativo de Home Assistant (HAOS). Hoy en día hay dos opciones recomendadas:

| Dispositivo | Precio Aprox. | Pros y Contras | ¿Recomendado? |
| :--- | :---: | :--- | :---: |
| **Raspberry Pi 4 / 5** | 80€ - 100€ | Consume poquísimo. **Contra:** Necesita tarjeta SD (que se acaban corrompiendo) o comprar un SSD aparte. Ha subido mucho de precio. | 🟡 Regular |
| **Home Assistant Green** | ~100€ | Es el hardware oficial. Plug & Play, ya viene instalado. Ideal si no quieres complicarte montando piezas. | 🟢 Sí |
| **Mini PC (Intel N100)**<br>*(Beelink, NiPoGi...)* | 150€ - 180€ | **El rey actual**. Trae disco duro NVMe (no falla como las SD), 16GB de RAM, muchísimo más potente que una Raspberry y su consumo eléctrico es ínfimo (6-10W). | ⭐ **La mejor opción** |

### 2. El Coordinador Zigbee (El "Antenista")

Para no saturar el Wi-Fi de tu casa con 30 bombillas, la domótica profesional usa el protocolo **Zigbee** (crea una red de malla independiente). Home Assistant necesita una antena USB para hablar Zigbee.

- **Recomendación:** *Sonoff Zigbee 3.0 USB Dongle Plus* (Versión E o P).
- **Precio:** ~25€ en Amazon (~15€ en AliExpress).

---

## 3. Sensores y Actuadores (Ejemplo Habitación)

Volviendo al objetivo: *Habitación que se ilumina sola si hay alguien.*

### El Sensor: PIR vs mmWave

| Sensor PIR (Movimiento clásico) | Sensor mmWave (Presencia por radar) |
| :--- | :--- |
| Solo detecta cambios bruscos de temperatura (movimiento grande). | Usa ondas de radar milimétricas (como los radares de los coches). |
| **Problema:** Si estás sentado estudiando quieto, leyendo o en el PC, el sensor cree que te has ido y **te apaga la luz**. Tienes que levantar los brazos para que te vea. | Detecta micromovimientos: **tu respiración, el latido del corazón o teclear**. Nunca te apagará la luz mientras estés en la habitación. |
| **Precio:** Barato (~10€) | **Precio:** Más caros, pero valen la pena para habitaciones en las que pasas mucho tiempo. |

#### Opciones de compra para mmWave:
1. **Aqara FP2 (Wi-Fi):** ~80€. Es el mejor del mercado. Permite dividir la habitación en zonas (si estoy en la cama enciende luz roja, si estoy en el escritorio enciende luz blanca).
2. **Tuya/Moes mmWave (Zigbee):** ~30€. Más barato pero requiere el pincho Zigbee de Sonoff para hablar con Home Assistant.

### La Bombilla (Actuador)
- **Ikea TRÅDFRI (Zigbee):** ~10€. Fiables, baratas y amplían la red Zigbee.
- **Tapo L530E (Wi-Fi):** ~10€. Colores RGB, muy buenas, directas al Wi-Fi.

---

## 4. Presupuestos Estimados

### 🛒 Presupuesto "Pro" (Home Assistant Local)
Si quieres montarte el laboratorio completo, aprender y no depender de internet:

1. **Mini PC Intel N100:** ~150€
2. **Antena Sonoff Zigbee USB:** ~25€
3. **Sensor mmWave Zigbee (Tuya):** ~30€
4. **Bombilla Zigbee IKEA:** ~10€
**TOTAL:** **~215€** *(Pero a partir de aquí, cada habitación extra solo te cuesta 40€)*.

### 🛒 Presupuesto "Fácil" (Sin Home Assistant)
Si solo quieres la habitación, todo por Wi-Fi usando la app oficial (depende de internet):

1. **Sensor Tapo Inteligente (T100, es PIR, no mmWave):** ~18€
2. **Hub Tapo H100 (Obligatorio para el sensor):** ~20€
3. **Bombilla Tapo L530E:** ~10€
**TOTAL:** **~48€** *(Limitado a la app de Tapo y con sensor PIR que te puede apagar la luz si estás quieto).*

> [!NOTE] Cuidado con los ecosistemas Wi-Fi
> Llenar la casa de dispositivos Wi-Fi (como 20 bombillas Tapo) puede saturar el router de tu operadora, haciendo que Netflix o tus juegos vayan mal. Por eso, a largo plazo, siempre se usa Zigbee + Home Assistant.

---

## 5. Ejemplo de Automatización Avanzada en Home Assistant

Una vez montado, la lógica gráfica en Home Assistant se ve así (sin picar código, aunque por detrás genera YAML):

```yaml
# Si la habitación detecta presencia
trigger:
  - platform: state
    entity_id: sensor.mmwave_habitacion
    to: "detected"
# Y es de noche (condición)
condition:
  - condition: time
    after: "23:00:00"
    before: "07:00:00"
# Entonces:
action:
  - service: light.turn_on
    target:
      entity_id: light.bombilla_habitacion
    data:
      brightness_pct: 15 # Enciende al 15% para no deslumbrar
      color_name: red
```
