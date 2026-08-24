
# **Que es el UserControl?**

En vez de ser una ventana entera como `Window` 
![[Pasted image 20251231034343.png]]
Se define una mini ventana con UserControl
![[Pasted image 20251231034412.png]]
Esto es para abrir solo un trozo de interfaz en vez de otra ventana nueva, para así hacer una **navegación dinámica** y hacerlo más moderno y fluido.

Ejemplo de como se vería:
![[Pasted image 20251231034628.png]]
Todo lo que ves esta en `MainWindow.xaml` que tiene `Window`
Por otro lado, `Principal` y `Mapa de Red` tienen `UserControl`


# 🔄 El Ciclo de Navegación Dinámica

Para que el contenido cambie sin abrir ventanas nuevas, el programa sigue estos tres pasos clave:

### 1. El Disparador: Botón → Command → Cambia CurrentView

Todo empieza con la acción del usuario. En la barra de menú del **MainWindow.xaml**, tenemos un botón conectado a un comando:

- **Acción:** Le damos al botón `Principal
    
- **Comando:** El botón dispara el `ShowMainCommand` que está en el **MainWindowViewModel**.
- ![[Pasted image 20251231035904.png]]
    
- **Método:** Este comando ejecuta el método `ExecuteShowMain`.
![[Pasted image 20251231040005.png]]
![[Pasted image 20251231035942.png]]
    
- **Cambio de valor:** Dentro de ese método, hacemos `CurrentView = new PrincipalViewModel();`. En este momento, el objeto llamado `CurrentView` ya contiene el objeto del ViewModel que queremos mostrar.


### 2. El Detector: ContentControl detecta el tipo

En el centro de nuestro **MainWindow.xaml**, tenemos al `ContentControl`.

- **Comunicación:** El `ContentControl` tiene un Binding a la propiedad `CurrentView`.
    
- **Detección:** Gracias a la notificación (`OnPropertyChanged`), el `ContentControl` se entera de que el objeto ha cambiado. A estas alturas, el programa ya sabe exactamente qué tipo de ViewModel tiene entre manos (en este caso, un `PrincipalViewModel`).
    

### 3. El Traductor: DataTemplate carga la View correcta

Aquí es donde ocurre la magia visual. El `ContentControl` sabe que tiene un `PrincipalViewModel`, pero no sabe cómo dibujarlo. Entonces acude a los **Resources** de la ventana:

- **Búsqueda:** WPF busca un `DataTemplate` cuyo `DataType` coincida con `PrincipalViewModel`.
    
- **Carga:** Al encontrarlo, ve que dentro del template dice `<views:PrincipalView />`.
    
- **Renderizado:** El programa quita lo que hubiera antes en el centro de la pantalla y proyecta el **UserControl** `PrincipalView` en ese lugar.

---

### 💡 El detalle de diseño: `d:DesignInstance`

- Usas la línea `d:DataContext="{d:DesignInstance Type=viewmodels:PrincipalViewModel}"`.
    
- **¿Para qué?** Para que el editor visual de Visual Studio tenga en cuenta que ya tiene cargado el ViewModel. Así puedes ver cómo quedan los botones y textos con datos de prueba sin tener que ejecutar el programa, si no pones esa linea y quieres ver el diseño te tocaría ejecutarlo.

![[Pasted image 20251231040239.png]]