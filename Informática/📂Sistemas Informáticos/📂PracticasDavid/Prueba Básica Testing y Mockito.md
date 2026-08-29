# **Memoria del Proyecto: Gestión de Socios de Gimnasio con Testing**

## **1. Objetivo del Proyecto**

El objetivo principal de este proyecto es **crear un backend para gestionar socios de un gimnasio**, y además **aprender a testearlo correctamente** usando buenas prácticas de desarrollo:

- Separación de responsabilidades (arquitectura en capas).
 
- Validación de datos y reglas de negocio.
 
- Pruebas unitarias con JUnit 5.
 
- Simulación de dependencias con Mockito para tests más fiables.
 
- Preparación para pruebas de la capa web con Javalin.
 

## **2. Arquitectura del Sistema**

Dividimos el sistema en **tres capas**, cada una con una responsabilidad clara:

### **2.1. Capa de Datos: Repositorio**

- Clase: `RepositorioSocios`
 
- Función: Guardar y recuperar socios.
 
- Cómo funciona:
 
 - Actúa como el “bibliotecario” de los datos.
 
 - La capa de negocio no necesita saber si los datos están en memoria, base de datos o archivos.
 
- Beneficios:
 
 - Desacoplamiento: puedes cambiar la forma de almacenar datos sin afectar la lógica de negocio.
 
 - Testabilidad: puedes usar implementaciones en memoria o mocks para pruebas.
 



![[Prueba Básica Testing y Mockito.png]]


### **2.2. Capa de Negocio: Servicio**

- Clase: `ServicioSocios`
 
- Función: Contiene todas las **reglas de negocio**.
 
- Ejemplos de reglas:
 
 1. El nombre no puede estar vacío.
 
 2. El email debe contener `@`.
 
 3. El email debe ser único.
 
- Beneficio: centraliza toda la lógica antes de tocar la base de datos o exponer un endpoint.
 

![[Prueba Básica Testing y Mockito-1.png]]



### **2.3. Capa Web: Controlador**

- Clase: `SociosController`
 
- Función: Recibe las peticiones HTTP y llama al servicio.
 
- Herramienta usada: Javalin (microframework Java para APIs REST).
 
- Beneficio: desacopla la lógica de negocio de la interacción con HTTP.
 

![[Prueba Básica Testing y Mockito-2.png]]



## **3. Tests: Cómo probamos cada capa**

### **3.1. Tests de la Capa de Negocio (Unit Tests)**

Clase: `ServicioSociosTest`

- Objetivo: asegurarnos de que **las reglas de negocio funcionan correctamente**.
 
- Estrategia: usamos **una implementación en memoria** de `RepositorioSocios` para aislar la lógica.
 

#### **Ejemplo: Camino Feliz**

![[Prueba Básica Testing y Mockito-3.png]]


#### **Ejemplo: Reglas de negocio**

![[Prueba Básica Testing y Mockito-4.png]]



### **3.2. Tests con Mocks**

Clase: `ServicioSociosTestConMocks`

- Objetivo: **simular el repositorio** para pruebas más rápidas y profesionales.
 
- Herramienta: Mockito (`@Mock` y `@InjectMocks`).
 

#### **Ejemplo: Email duplicado con mock**

![[Prueba Básica Testing y Mockito-5.png]]


- **Beneficio**: No dependemos de datos reales, todo es rápido y controlable.
 


### **3.3. Tests de la Capa Web**

Clase: `SociosControllerTest`

- Objetivo: verificar que el **controlador responde correctamente a Javalin**.
 
- Estrategia: simular el objeto `Context` de Javalin con Mockito.
 

![[Prueba Básica Testing y Mockito-6.png]]


- Verifica:
 
 1. Se llama al servicio.
 
 2. Se devuelve el código HTTP correcto (201).
 
 3. Se devuelve el JSON correcto.
 