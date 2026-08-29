El **ViewModel** es la capa que se encarga de toda la gestión de la interfaz de usuario. Es el intermediario entre el View y el Model haciendo que no se comuniquen entre si.

Toma los datos del **Model** (la base de datos), los prepara para que la **View** (la pantalla) los entienda, y gestiona las notificaciones para que todas las capas se comuniquen entre sí.

Aquí tienes el flujo paso a paso:

1. **Entrada (Usuario → View → VM):** El usuario escribe "Juan" en el `TextBox`. El **Binding** envía ese dato a la propiedad `Nombre` del **ViewModel**.
 
2. **Lógica (VM → Model):** El **ViewModel** recibe "Juan" y lo guarda dentro de su objeto privado del modelo (`telefono.Nombre = value`). Ahora el objeto del **Model** tiene el dato.
 
3. **El "Grito" (VM → View):** Justo después de guardar el dato en el modelo, el **ViewModel** ejecuta `OnPropertyChanged()`. Esto es como un grito que dice: _"¡Atención, la propiedad Nombre ha cambiado!"_.
 
4. **Refresco automático (View ← VM):** La **View**, que está escuchando ese grito, vuelve a leer la propiedad `Nombre` del **ViewModel**. Como el **ViewModel** ya tiene el dato actualizado en su objeto del modelo, le devuelve "Juan" a la pantalla.

### 📄 3.1 BaseViewModel 

Lo primero que hacemos es crear una clase base llamada **BaseViewModel**. Esta clase se define como pública y abstracta para que no se pueda usar directamente, sino que sirva únicamente para que el resto de nuestros ViewModels hereden de ella.

**¿Para qué sirve?** 
Implementamos aquí la interfaz `INotifyPropertyChanged`.
![[Pasted image 20251231020620.png]]
Al hacerlo en la base, nos aseguramos de que cualquier ViewModel que hagamos después heredará automáticamente el método **OnPropertyChanged**. Este método es el que se encarga de enviar una "notificación" a la interfaz cada vez que escribimos o cambiamos un dato en el código, permitiendo que los atributos se actualicen en tiempo real.

---

### 📄 3.2 TelefonosViewModel (La lógica de negocio)

Aquí es donde ocurre la comunicación real entre la vista de teléfonos y sus datos. Para que la **View** pueda acceder a la información, no usamos variables sueltas, sino que creamos propiedades públicas con sus respectivos **get y set**.


Estas propiedades suelen apuntar directamente a un objeto del modelo como por ejemplo:
![[Pasted image 20251231020759.png]]

- **El Get:** Permite que la vista lea el valor almacenado.
 
- **El Set:** Es la parte crítica. En el momento en que el usuario escribe en la pantalla y cambia la variable, el `set` captura ese valor y llama inmediatamente al método **OnPropertyChanged**.

![[Pasted image 20251231020816.png]]


Este flujo es el que garantiza que, gracias al **Binding** que pusimos en el XAML, el cambio se refleje al momento sin necesidad de refrescar la ventana manualmente.

---

### 📄 3.3 RelayCommand: El sustituto de los eventos

Dentro de la carpeta `/Base` también incluimos la clase **RelayCommand**. En MVVM, en el code behind, ya no usamos el típico evento Click. En su lugar, usamos **Commands**.

El **RelayCommand** es una herramienta que nos permite encapsular una acción (como Guardar o Borrar) dentro de un objeto que el ViewModel puede manejar. Tiene dos funciones principales:

1. **Execute:** Es la acción que se ejecuta cuando pulsas el botón (ej. llamar al servicio para insertar en la DB).
![[Pasted image 20251231021007.png]]
 
2. **CanExecute:** Es una validación que devuelve un valor verdadero o falso. Si es falso, WPF deshabilitará el botón automáticamente (por ejemplo, si el campo de teléfono está vacío, el botón de "Guardar" se verá gris y no se podrá pulsar).
![[Pasted image 20251231021035.png]]

Este código siempre es copiar y pegar.

---