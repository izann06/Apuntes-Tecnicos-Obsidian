ERROR NO SE SINCRONIZA EL GRADLE 

# 1. El botón "Elefante" (Sync Project with Gradle Files)

Si no ves la barra superior con el icono del elefante, haz lo siguiente:

**Ve al menú superior: File -> Sync Project with Gradle Files.**


# 2 Forzar el re-importado del Gradle

Cierra Android Studio.

Ve a la carpeta de tu proyecto en el explorador de archivos de Windows.

Busca y borra la carpeta oculta llamada.gradle (está en la raíz).

Busca y borra la carpeta oculta llamada.idea.

Tranquilo, no borras tu código, solo la configuración de memoria de Android Studio.

Vuelve a abrir Android Studio y dale a File -> Open y selecciona el archivo build.gradle.kts de la raíz de tu proyecto.

# 3. Cambiar la vista del explorador
A veces el proyecto está bien, pero simplemente se ha cambiado la vista:

Arriba a la izquierda, justo encima de la lista de archivos, verás un desplegable que quizá dice "Project" o "Packages".

Haz clic y selecciona "Android".