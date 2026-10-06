#sistemas #hardware #discos-opticos #blu-ray #dvd #cd #almacenamiento-optico

> [!info] Navegación
> 🔗 Relacionado: [[Formatos de Imagen Explicados (JPG, PNG, SVG, RAW, WebP y más)|Formatos de Imagen]] | [[Componentes del PC Explicados|Componentes del PC]]

---

# Todos los Discos Ópticos Explicados

La historia del almacenamiento óptico es la historia de cómo la humanidad aprendió a grabar información con luz. Desde los discos analógicos de 30 cm de los años 70 hasta el Blu-ray UHD de 100 GB actual.

---

## 💡 Cómo Funciona un Disco Óptico (Base)

Todos los discos ópticos funcionan bajo el mismo principio: un **láser** lee (y en los grabables, también escribe) datos en una superficie reflectante mediante **pits** (hoyos microscópicos) y **lands** (superficies planas).

```mermaid
flowchart LR
    L["🔴 Láser"] --> D["💿 Superficie del disco"]
    D --> R["Sensor de reflexión"]
    R --> |"Pit = poca reflexión"| P["0 lógico"]
    R --> |"Land = alta reflexión"| La["1 lógico"]
```

La longitud de onda del láser determina cuánto puede reducirse el tamaño de los pits → más pits = más datos almacenados. Por eso cada generación de disco usa un láser de menor longitud de onda (infrarrojo → rojo → azul-violeta).

---

## 📀 La Historia Completa

### LaserDisc (1978)

El pionero. El primer soporte óptico comercial para vídeo.

- **Tamaño:** 30 cm (como un LP de vinilo)
- **Capacidad:** ~1 GB por cara
- **Vídeo:** Analógico (no digital)
- **Audio:** Digital (¡era mejor que el VHS en audio!)
- **Uso:** Videoclubes de alta gama, coleccionistas. Nunca llegó al público masivo por el precio y el tamaño.

---

### CD-DA (Compact Disc Digital Audio - 1982)

Desarrollado por **Philips y Sony**. La revolución del audio digital.

- **Tamaño:** 12 cm
- **Capacidad:** 700 MB / 80 minutos de audio
- **Especificación de audio:** 16 bits a 44.1 kHz (el estándar que define la calidad de audio digital hoy)
- **Láser:** Infrarrojo (780 nm)
- **Impacto:** Sustituyó al vinilo y al cassette como formato de música dominante durante los años 80 y 90.

---

### CD-ROM (1985)

La versión del CD para datos de ordenador (Read-Only Memory).

- **Capacidad:** 650-700 MB
- **Velocidad de referencia (1x):** 150 KB/s. Los lectores modernos llegaron a 52x (7.8 MB/s)
- **Uso:** Distribución de software, videojuegos (PC, PlayStation 1), enciclopedias multimedia.

---

### CD-R y CD-RW

Las variantes grabables:

| Formato | Tecnología | Regrabable | Uso |
|---|---|---|---|
| **CD-R** | Tinte orgánico sensible al láser que se "quema" permanentemente | No | Grabación única de datos o música |
| **CD-RW** | Aleación de cambio de fase (reversible con calor) | Sí (~1000 veces) | Borradores, transporte de datos temporales |

---

### VCD — Video CD (1993)

Vídeo estándar comprimido en MPEG-1 en un CD normal.

- **Calidad:** ~VHS (resolución 352x240, bitrate bajo)
- **Capacidad:** 74 minutos de vídeo por disco
- **Dominante en Asia en los años 90**, nunca tuvo gran adopción en Europa/América.

---

### MiniDisc (1992, Sony)

El intento de Sony de crear el sucesor del cassette.

- **Tamaño:** Disco de 6.4 cm en cartucho protector rígido
- **Tecnología:** Magneto-óptico (se escribe con campo magnético + láser, se lee solo con láser)
- **Capacidad:** 80 minutos de audio con compresión ATRAC
- **Éxito:** Moderado, especialmente en Japón. Nunca sustituyó al CD globalmente.
- **Final:** Sony lo discontinuó en 2013.

---

### DVD (1995-1996)

El sucesor del CD, diseñado para vídeo de alta calidad.

- **Láser:** Rojo (650 nm) — longitud de onda menor que CD → pits más pequeños → más densidad
- **Capacidad:** 4.7 GB (capa simple) / 8.5 GB (doble capa, DVD-DL) / 9.4 GB (doble cara)
- **Vídeo:** MPEG-2, resolución 480p/576p (estándar de definición)
- **Audio:** Dolby Digital, DTS (multicanal)

**Variantes de grabación:**

| Formato | Observaciones |
|---|---|
| **DVD-R / DVD+R** | Grabación única. La guerra de formatos (- vs +) fue resuelta por los grabadores multi-formato |
| **DVD-RW / DVD+RW** | Regrabables |
| **DVD-RAM** | Regrabable de alta durabilidad, acceso aleatorio real. Usado en videograbadoras domésticas |

---

### Formatos de Consola

#### GD-ROM (Sega Dreamcast, 1998)

- **Gigabyte Disc**: Modificación del CD-ROM estándar con mayor densidad → 1 GB de capacidad
- Diseñado para dificultar la piratería (los lectores de CD normales no podían leerlos directamente)

#### UMD — Universal Media Disc (Sony PSP, 2004)

- Disco óptico en cartucho de 6 cm: 1.8 GB de capacidad
- Solo lectura, diseñado exclusivamente para la PSP
- Formato discontinuado con la PSP (la Vita no lo soportó)

---

### Blu-ray (2006)

El formato de alta definición que ganó la "guerra del HD" frente al HD-DVD.

> [!note] ¿Por qué "Blu-ray"?
> Usa un **láser azul-violeta (405 nm)** — longitud de onda mucho menor que el DVD (650 nm). Longitud de onda menor = pits más pequeños = mucho más datos en el mismo disco.

- **Capacidades:**
  - BD-25: 25 GB (capa simple)
  - BD-50: 50 GB (doble capa)
  - BD-100 (BDXL): 100 GB (triple capa, usado en másters)
- **Vídeo:** H.264 / VC-1, resolución hasta 1080p
- **Audio:** Dolby TrueHD, DTS-HD Master Audio (sin pérdida)
- **Protección de copia:** AACS + BD+

---

### Ultra HD Blu-ray (2016)

La evolución para el ecosistema 4K HDR.

- **Capacidad:** 66 GB (doble capa) / 100 GB (triple capa)
- **Vídeo:** HEVC (H.265), resolución **4K (3840×2160)**, **HDR10**, Dolby Vision
- **Audio:** Idéntico al Blu-ray estándar (TrueHD, DTS-HD MA)
- **Importante:** Un reproductor Ultra HD Blu-ray puede reproducir también discos Blu-ray normales y DVD, pero no al revés.

---

## 📊 Tabla Resumen Completa

| Formato | Año | Capacidad | Láser | Resolución vídeo |
|---|---|---|---|---|
| LaserDisc | 1978 | ~1 GB/cara | IR analógico | Analógica |
| CD-DA / CD-ROM | 1982/85 | 700 MB | IR (780 nm) | — |
| CD-R / CD-RW | 1988/97 | 700 MB | IR (780 nm) | — |
| VCD | 1993 | 700 MB | IR (780 nm) | ~240p |
| MiniDisc | 1992 | ~140 MB | IR (780 nm) | — |
| DVD | 1996 | 4.7-8.5 GB | Rojo (650 nm) | 480p/576p |
| GD-ROM | 1998 | ~1 GB | IR modificado | — |
| UMD | 2004 | 1.8 GB | Azul (405 nm) | — |
| **Blu-ray** | **2006** | **25-100 GB** | **Azul (405 nm)** | **1080p** |
| **UHD Blu-ray** | **2016** | **66-100 GB** | **Azul (405 nm)** | **4K HDR** |

> [!tip] 💡 El declive del físico
> El streaming (Netflix, Disney+, Spotify) ha reducido el mercado físico a coleccionistas y audiófilos. Sin embargo, el Blu-ray UHD sigue siendo la referencia en calidad de imagen y sonido: ningún servicio de streaming ofrece actualmente la misma calidad de bitrate que un UHD Blu-ray físico.
