### ¿Qué son y por qué son diferentes?

Con un fichero de texto (.txt) Java traduce los 0s y 1s del disco a letras que tú entiendes. Un **fichero binario** (.jpg, .mp3, .pdf, .exe) es **información cruda**.

- **No hay traducción:** Si intentas leer una imagen con un `FileReader`, Java intentará buscar letras donde no las hay y **corromperá** el archivo.
    
- **Unidad de medida:** El **Byte**. Un número entero del 0 al 255.
    
- **La Clave:** Usamos clases que terminan en **Stream** (Flujo).
    

> **⚠️ Regla de Oro:**
> 
> - ¿Es algo que puedes abrir y leer en el Bloc de Notas? -> Usa **Reader/Writer**.
>     
> - ¿Es cualquier otra cosa (imagen, sonido, programa)? -> Usa **InputStream/OutputStream**.


# **LECTURA DE BINARIO (Input)**

Para leer archivos de binario tenemos:

* FileInputStream
* BufferedInputStream
* DataInputStream

## **FileInputStream** 

La clase FileInputStream en Java forma parte del paquete java.io y se utiliza para leer datos en bruto desde un archivo. Opera a nivel de bytes, por lo que es adecuada para leer datos binarios como imágenes, audio, vídeo o cualquier tipo de archivo que no sea de texto plano.

### Lectura (`FileInputStream`)

- **`read()`**: Lee **un solo byte**.
    
    - Devuelve un `int` entre 0 y 255.
        
    - Devuelve **`-1`** si ha llegado al final del archivo.
        
- **`read(byte[] buffer)`**: Lee un bloque de bytes y los mete en un array. Devuelve el número de bytes que ha conseguido leer.

![[Pasted image 20251217142459.png]]


## **BufferedInputStream** 

Mejora el rendimiento de FileInputStream al utilizar un buffer intermedio. Es útil cuando se trabaja con archivos grandes.(Aquí usa el método **read** como en FileInputStream,recordemos que en BufferedReader usaba **readLine**())

![[Pasted image 20251217142830.png]]


## **DataInputStream** 

Permite leer datos primitivos de manera más cómoda (int, double, char, etc.) a partir de un InputStream.

![[Pasted image 20251217142901.png]]
![[Pasted image 20251217142908.png]]



# **ESCRITURA DE BINARIO (Output)**

Para leer archivos de binario tenemos:

* FileOutputStream
* BufferedOutputStream
* DataOutputStream

## **FileOutputStream** 

- Escribe **bytes puros** en un archivo.
    
- Se usa directamente para datos binarios

![[Pasted image 20251217143755.png]]

## **BufferedOutputStream** 

- **Envuelve** un `OutputStream` (como `FileOutputStream`) para **escribir más rápido**.
    
- Usa un **buffer interno** y reduce llamadas al disco.

![[Pasted image 20251217143827.png]]


## **DataOutputStream** 

- Escribe **tipos primitivos** (int, double, boolean…) en **binario directamente**.
    
- Muy útil para archivos que se van a leer con `DataInputStream`.

![[Pasted image 20251217143852.png]]

