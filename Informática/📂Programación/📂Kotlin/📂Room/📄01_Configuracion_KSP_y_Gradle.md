Para usar ROOM hoy en día, necesitamos configurar el procesador de anotaciones **KSP** y añadir las dependencias correctas. Esto se hace en dos archivos `build.gradle.kts` diferentes.

## 1. Archivo `build.gradle.kts` (Project)

Primero, debemos declarar el plugin KSP a nivel global del proyecto.

> [!WARNING] Versiones La versión de KSP debe coincidir con tu versión de Kotlin.
> 
> - Ejemplo del temario: `2.2.0-2.0.2` (significa KSP 2.2.0 para Kotlin 2.0.2).
>     
> - Revisa la [GitHub de KSP](https://github.com/google/ksp/releases) si cambias la versión de Kotlin.
>     

![[Pasted image 20260114133243.png]]

```
plugins {
    // ... otros plugins
    id("com.google.devtools.ksp") version "2.2.0-2.0.2" apply false
}
```

---

## 2. Archivo `build.gradle.kts` (Module :app)

Ahora vamos al archivo del módulo (donde están las dependencias) y hacemos dos cosas: activar el plugin y añadir las librerías.

### A. Activar el Plugin

Al principio del archivo:
![[Pasted image 20260114133254.png]]

```
plugins {
    // ...
    id("com.google.devtools.ksp")
}
```

### B. Añadir Dependencias

En el bloque `dependencies`. Fíjate que usamos `ksp(...)` en lugar de `implementation(...)` para el compilador.

![[Pasted image 20260114133327.png]]

```
dependencies {
    // --- ROOM (Base de Datos) ---
    implementation("androidx.room:room-runtime:2.7.2")
    implementation("androidx.room:room-ktx:2.7.2") // Soporte para Corrutinas y Flow
    ksp("androidx.room:room-compiler:2.7.2")       // El procesador de anotaciones (KSP)

    // --- LIFECYCLE & VIEWMODEL ---
    implementation("androidx.lifecycle:lifecycle-viewmodel-ktx:2.9.2")
    implementation("androidx.lifecycle:lifecycle-viewmodel-compose:2.9.2")
    
    // --- NAVEGACIÓN ---
    implementation("androidx.navigation:navigation-compose:2.9.3")
}
```

> [!TIP] Sync Now No olvides pulsar el botón del "Elefantito" 🐘 (Sync Project with Gradle Files) después de pegar estos códigos para que se descarguen las librerías.