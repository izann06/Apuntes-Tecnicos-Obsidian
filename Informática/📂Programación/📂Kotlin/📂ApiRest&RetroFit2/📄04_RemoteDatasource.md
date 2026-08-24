El **RemoteDatasource** es el encargado directo de ejecutar las llamadas a la API. Actúa como una capa de abstracción sobre `Retrofit`.

## 1. ¿Por qué existe esta clase?

Podríamos llamar a Retrofit directamente desde el Repositorio, pero crear un `Datasource` tiene ventajas:

- **Desacoplamiento:** Si mañana decides cambiar Retrofit por otra librería (como Ktor), solo tienes que cambiar este archivo. El resto de tu app ni se entera.
    
- **Limpieza:** El Repositorio no debe saber cómo se conecta a internet, solo qué datos necesita. Cada clase debe hacer una cosa es clave en la organización y claridad de todo proyecto.
    

---

## 2. El Código (RemoteDatasource.kt)

Esta clase es muy sencilla. Simplemente instancia el servicio y expone sus funciones.

![[Pasted image 20260113234259.png]]

> [!TIP] Diferencia con LocalDatasource En una arquitectura completa, tendrías también un `LocalDatasource` (para ROOM).
> 
> - **RemoteDatasource:** Pide datos a la nube ☁️.
>     
> - **LocalDatasource:** Pide datos al disco duro del móvil 💾. El **Repository** será quien coordine a ambos.
>     

---

## 3. Flujo de llamada simplificado

Hasta ahora, nuestra cadena de llamadas se ve así:

**`RemoteDatasource`** -> llama a -> `RetrofitClient` -> llama a -> `Internet`.

