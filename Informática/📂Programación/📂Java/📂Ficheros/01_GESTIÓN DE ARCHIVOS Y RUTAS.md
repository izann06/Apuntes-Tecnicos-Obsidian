
Tenemos dos formas en la que Java interactúa con el disco para manejar la estructura de archivos. Hay dos formas de hacerlo la clásica **(IO)** y la moderna **(NIO)**.

## 1. La Forma Clásica: Java IO (`java.io.File`)

### ¿Qué es y cuál es su función?

La clase File de Java forma parte del paquete java.io y se utiliza para representar rutas de archivos y directorios en el sistema de archivos. No proporciona métodos para leer o escribir directamente en los archivos, sino que sirve como un objeto abstracto que describe la ruta y permite realizar operaciones relacionadas con la gestión de archivos.

## Características principales
Algunas de las características más importantes de la clase File son: 
• Representa rutas de archivos y directorios, tanto **relativos** como **absolutos**. 
• Permite **crear**, **eliminar** y **renombrar** archivos o directorios. 
• Proporciona métodos para comprobar permisos de lectura, escritura y ejecución. 
• Permite **obtener información** como tamaño, fecha de modificación y ruta absoluta. 
• Puede **listar** los archivos contenidos en un directorio.

**Problema principal:** Muchos de sus métodos devuelven `false` cuando fallan en lugar de lanzar una excepción explicativa, por lo que a veces es difícil saber por qué no se ha podido crear un archivo.

### 🛠 Métodos más usados de `File`

|**Método**|**Descripción**|
|---|---|
|`exists()`|Devuelve `true` si el archivo/directorio existe realmente.|
|`createNewFile()`|Crea un archivo vacío. Lanza excepción si hay error de disco.|
|`mkdir()`|Crea un directorio. (Solo el último de la ruta).|
|`mkdirs()`|Crea un directorio y **todos los padres** necesarios si no existen.|
|`delete()`|Borra el archivo o directorio (solo si el directorio está vacío).|
|`getName()`|Devuelve el nombre (ej: "notas.txt").|
|`getAbsolutePath()`|Devuelve la ruta completa (ej: `C:\Users\...\notas.txt`).|
|`isDirectory()`|`true` si es una carpeta.|
|`isFile()`|`true` si es un archivo normal.|
|`listFiles()`|Devuelve un array `File[]` con el contenido de una carpeta.|
**Ejemplo de comprobar que hay dentro de una carpeta:**

**Código**

![[Pasted image 20251217123712.png]]

**Resultado**

![[Pasted image 20251217123803.png]]

**Lo que había**

![[Pasted image 20251217124006.png]]



## 2. La Forma Moderna: Java NIO (`java.nio.file`)

### ¿Qué es y cuál es su función?

La N significa **N**ew **I/O** (Nuevo Input/Output), introducido en Java 7 para arreglar los problemas de la clase `File`. Es mucho más potente, maneja mejor los errores y es más escalable.

En NIO, se separan los conceptos en dos clases principales:

1. **`Path` (Interfaz):** Es la **dirección** del archivo (sustituye al objeto `File`).

2. **`Files` (Clase de utilidad):** Es el **trabajador**. Tiene métodos estáticos que hacen las acciones (`Files.create...`, `Files.delete...`).

### Métodos más usados de `Files` y `Path`

Primero, para obtener una ruta usamos: 
`Path ruta = Paths.get("archivo.txt");`
`Path ruta = Paths.get("carpeta/archivo.txt");`

|**Método de la clase Files**|**Descripción**|
|---|---|
|`Files.exists(Path p)`|Comprueba si la ruta existe.|
|`Files.createFile(Path p)`|Crea el archivo. Si ya existe, **lanza excepción**.|
|`Files.createDirectory(Path p)`|Crea una carpeta.|
|`Files.createDirectories(Path p)`|Equivalente a `mkdirs()` (crea padres también).|
|`Files.delete(Path p)`|Borra. Si no existe o no está vacío, **lanza excepción**.|
|`Files.copy(Path origen, Path destino)`|Copia un archivo (algo que `File` no sabía hacer).|
|`Files.move(Path origen, Path destino)`|Mueve o renombra un archivo.|


# EL DUELO: IO vs NIO (Mismo código)

Vamos a resolver el mismo ejercicio con ambas tecnologías para que vet la diferencia.

**Ejercicio:**

1. Crear una carpeta llamada "MiCarpeta".
 
2. Dentro, crear un archivo llamado "secreto.txt".
 
3. Mostrar la ruta absoluta del archivo.
 

### Opción A: Código con Java IO (Clásico)



```
import java.io.File;
import java.io.IOException;

public class EjemploIO {
 public static void main(String[] args) {
 // 1. Definir la carpeta y el archivo
 File carpeta = new File("MiCarpeta");
 File archivo = new File(carpeta, "secreto.txt");

 // 2. Crear carpeta
 if (!carpeta.exists()) {
 if (carpeta.mkdir()) {
 System.out.println("Carpeta creada (IO).");
 } else {
 System.out.println("Error al crear carpeta.");
 }
 }

 // 3. Crear archivo
 try {
 if (archivo.createNewFile()) {
 System.out.println("Archivo creado (IO).");
 } else {
 System.out.println("El archivo ya existía.");
 }
 // 4. Mostrar ruta
 System.out.println("Ruta: " + archivo.getAbsolutePath());
 
 } catch (IOException e) {
 e.printStackTrace();
 }
 }
}
```

### Opción B: Código con Java NIO (Moderno)

Java

```
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.io.IOException;

public class EjemploNIO {
 public static void main(String[] args) {
 // 1. Definir las Rutas (Path)
 Path rutaCarpeta = Paths.get("MiCarpeta");
 Path rutaArchivo = rutaCarpeta.resolve("secreto.txt"); // Une las rutas

 try {
 // 2. Crear carpeta (crea directorios padres si hace falta automáticamente)
 if (Files.notExists(rutaCarpeta)) {
 Files.createDirectories(rutaCarpeta);
 System.out.println("Carpeta creada (NIO).");
 }

 // 3. Crear archivo
 if (Files.notExists(rutaArchivo)) {
 Files.createFile(rutaArchivo);
 System.out.println("Archivo creado (NIO).");
 } else {
 System.out.println("El archivo ya existía.");
 }

 // 4. Mostrar ruta (toAbsolutePath devuelve Path, hay que pasar a String)
 System.out.println("Ruta: " + rutaArchivo.toAbsolutePath().toString());

 } catch (IOException e) {
 // NIO lanza excepciones más detalladas si falla algo
 e.printStackTrace();
 }
 }
}
```

### Conclusión:

- Si te piden **gestionar carpetas** o **copiar/mover** archivos: Usa **NIO** (`Files`), es mucho más potente.

- Si te piden simplemente comprobar si un archivo existe o sacar su nombre para un ejercicio sencillo: **IO** (`File`) suele requerir menos líneas de importación y código.