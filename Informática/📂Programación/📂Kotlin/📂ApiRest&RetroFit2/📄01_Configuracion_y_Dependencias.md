Para que nuestra aplicación pueda conectarse a internet y procesar datos, necesitamos instalar herramientas externas (librerías) y pedir permiso al sistema Android.

## 1. Las Dependencias (build.gradle.kts)

Debemos ir al archivo `build.gradle.kts` (Module: App) y añadir las siguientes librerías en el bloque `dependencies`.

> [!INFO] ¿Qué hace cada una?
> 
> - **Retrofit:** Es el cliente que conecta con la API.
>     
> - **Converter GSON:** Es el "traductor". Retrofit descarga JSON, y esta librería lo convierte en objetos Kotlin automáticamente.
>     
> - **Corrutinas:** Permiten hacer la llamada en segundo plano (asíncrono) para no congelar la pantalla.
>     
> - **ViewModel:** Nos ayuda a mantener los datos vivos aunque giremos la pantalla.
>     

**Copia estas dependencias:**

```
dependencies {
    // 1. ViewModel (Arquitectura MVVM)
    implementation("androidx.lifecycle:lifecycle-viewmodel-ktx:2.9.3")
    implementation("androidx.lifecycle:lifecycle-viewmodel-compose:2.9.3")

    // 2. Retrofit2 (El cliente HTTP)
    implementation("com.squareup.retrofit2:retrofit:3.0.0")

    // 3. Conversor JSON (Gson)
    implementation("com.squareup.retrofit2:converter-gson:3.0.0")

    // 4. Corutinas (Para no bloquear la UI)
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-android:1.10.2")
}
```
![[Pasted image 20260113130556.png]]
_Nota: Recuerda pulsar el botón **"Sync Now"** (el elefantito) después de pegar esto para que Android Studio descargue los archivos._

---

## 2. El Permiso de Internet (AndroidManifest.xml)

Por defecto, Android **bloquea** la salida a internet por seguridad. Tenemos que declarar explícitamente que nuestra app necesita salir al exterior.

Esto se hace en el archivo `AndroidManifest.xml`. La línea debe ir **fuera** de la etiqueta `<application>`, normalmente justo encima.

XML

```

<uses-permission android:name="android.permission.INTERNET" />

```
![[Pasted image 20260113130636.png]]
> [!DANGER] Error Común Si olvidas poner esta línea en el Manifest, la aplicación se cerrará inesperadamente (crash) al intentar hacer la petición, lanzando una `SecurityException`. **Regla de oro:** ¿Vas a usar Retrofit? -> Ve directo al Manifest primero.

---

## 3. Tráfico HTTP vs HTTPS

Hoy en día, casi todas las APIs son seguras (**HTTPS**), si alguna vez tienes que conectarte a una API antigua o local que sea solo **HTTP**, Android bloqueará la conexión por defecto.

>[!NOTE] OJO
 Investigar sobre el tema de **Apis con HTTP** si llego a usarlo y además plasmar la esa información a estos apuntes