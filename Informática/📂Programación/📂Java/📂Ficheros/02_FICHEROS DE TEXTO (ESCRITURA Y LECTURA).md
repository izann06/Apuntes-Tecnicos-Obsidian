Hay que diferenciar los archivos de texto con los archivos binarios ya que son dos cosas se leen y escriben distintas.

Es importante entender la diferencia por eso quiero explicarlo para entender luego los ficheros de texto y binarios a la perfección.

El disco solo guarda en bytes por lo que en los archivos de texto y binarios, dentro están compuestos por bytes.

En los archivos de texto usamos la codificación UTF-8 para convertir bytes a Char y así poder leerlo y hacerlo legible.

![[Pasted image 20251217125422.png]]

Por otro lado, los archivos binarios cada byte no representa una letra si no datos estructurados, además de que no tiene sentido hacer la traducción porque esos bytes no representan caracteres como en el texto ya que lo que se guarda ahí es:

* Música

* Imágenes

* Ejecutables(.exe)

* Videos

* PDFs

Si intentas convertir esos bytes a texto se corrompen esos archivos y si lo abres veras símbolos raros no legibles. Por eso, no se decodifica se leen los bytes exactamente igual que se guardaron.

Después de esta introducción de diferencia entre archivos de texto y binario ya podemos continuar.


# **LECTURA DE TEXTO (Input)**

El objetivo es leer y mostar lo que hay en el archivo.

Para leer archivos de texto tenemos:

* FileReader

* BufferedReader

* FilesAllLines

* Files.lines

* Scanner

## **FileReader** 

Permite leer caracteres directamente desde un archivo. Es adecuada para leer texto básico, pero normalmente se combina con BufferedReader para mejorar el rendimiento.

Lee con el método **read** y devuelve enteros.
Si da -1 termina porque un char nunca puede ser negativo, así que si da -1 es porque llegó al final del archivo.

![[Pasted image 20251217130526.png]]

## **BufferedReader** 

Permite leer texto de manera eficiente, especialmente línea por línea. Se suele utilizar junto con FileReader o InputStreamReader.

Esto es porque BufferedReader por si solo no abre archivos,él abre un buffer para almacenar(cubo),
y el FileReader es el que abre el archivo y lee los caracteres(agua).

Lee con el método **readLine** y devuelve strings.
Si da **null** es porque ha llegado al final del archivo.


![[Pasted image 20251217130605.png]]



## **Files.readAllLines** 

Esto es un método y lee todas las líneas de un archivo y las devuelve en una lista de Strings. Es una forma sencilla de obtener todo el contenido de un archivo **pequeño** o **mediano**.

![[Pasted image 20251217130720.png]]


## **Files.Lines**

- Pertenece a `java.nio.file.Files`.
 
- Devuelve un **Stream 'String'**, es decir, **líneas de texto**.
 
- **Se usa solo con archivos de texto**, porque interpreta los bytes como caracteres (por defecto UTF-8).

- 
![[Pasted image 20251217144313.png]]


## **InputStreamReader** 

Convierte un flujo de bytes en caracteres, permitiendo especificar una codificación como UTF-8. Se combina habitualmente con BufferedReader.

![[Pasted image 20251217144401.png]]

## **Scanner** 

Scanner se puede utilizar para leer archivos de texto de manera sencilla, línea a línea o token por token. Permite definir la codificación del archivo.



Se lee con el método hasNextLine que devuelve booleanos.
Básicamente si hay una línea (true) lee si no (false), termina.

![[Pasted image 20251217131201.png]]

Se puede usar de otra manera porque a veces no quieres leer líneas enteras, sino datos específicos mezclados (ej: "Nombre Edad"). Aquí `BufferedReader` es torpe y `Scanner` brilla.

**Métodos:** `.next()` (lee palabra), `.nextInt()` (lee entero), `.nextDouble()` (lee decimal)

![[Pasted image 20251217131734.png]]



# **ESCRITURA DE TEXTO (Output)**

El objetivo es escribir datos del programa en archivos.

Para leer archivos de texto tenemos:

* FileWriter

* BufferedWriter

* PrintWriter


## **FileWriter** 

Se utiliza para escribir caracteres en un archivo. Permite escribir directamente en el fichero, aunque no es la más eficiente al trabajar con grandes volúmenes de datos.

**INCISO**
Para escribir, hay que abrir un buffer y luego tenemos que cerrarlo para que no hayan errores,pérdidas de datos... Eso se hace con el metodo close(), pero con try-with-resources nos olvidamos de hacerlo y lo hace él automáticamente.

En este ejemplo está con el close, pero en los demás con el try para ver la diferencia.

![[Pasted image 20251217132135.png]]


## **BufferedWriter** 

Se utiliza junto con FileWriter para mejorar la eficiencia, ya que almacena los datos en un buffer antes de escribirlos en el archivo.

![[Pasted image 20251217132611.png]]


## **PrintWriter** 

Permite escribir texto en un archivo de manera más sencilla, similar a cómo funciona System.out.println.

Aquí implementamos al lado del archivo, el true que sirve para que borre lo que hay y se guarde en el fichero.
Ya que al cerrar el programa lo que había en el fichero se borra,con el true conseguimos mantenerlo.

![[Pasted image 20251217132905.png]]