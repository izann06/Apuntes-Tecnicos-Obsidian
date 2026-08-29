En esta sección implementamos la **validación mediante propiedades**utilizando la interfaz **`INotifyDataErrorInfo`**. Este método es el más robusto porque permite al **ViewModel** decidir qué es un error y notificárselo a la **View** de forma automática.

### 📄 6.1 Preparando la Base (BaseViewModel.cs)

Para no repetir código en cada ventana, añadimos la lógica de validación en nuestra clase base. Necesitamos tres cosas:

- **Un Diccionario:** Para guardar los errores de cada propiedad (ej. "Ntelefono" -> "No puede tener más de 9 dígitos").

- ![[Pasted image 20251231023109.png]]
 
- **El Evento `ErrorsChanged`:** Para avisar a la interfaz de que un error ha aparecido o desaparecido.

- ![[Pasted image 20251231023124.png]]
 
- **Métodos Auxiliares:** `AddError` para registrar un fallo y `ClearErrors` para limpiar los errores cuando el usuario corrige lo que escribió.

- ![[Pasted image 20251231023138.png]]![[Pasted image 20251231023148.png]]

### 📄 6.2 Implementación en el ViewModel (TelefonosViewModel.cs)

Una vez que la base está lista, validar es tan sencillo como poner un "filtro" en el **set** de nuestras propiedades públicas.

**¿Cómo funciona el flujo?**

1. El usuario escribe un número.
 
2. El `set` de la propiedad recibe el valor.
 
3. **Limpiamos errores previos:** Llamamos a `ClearErrors("Ntelefono")`.
 
4. **Evaluamos:** Si el número tiene más de 9 dígitos, llamamos a `AddError("Ntelefono", "Mensaje de error")`.
 
5. **Notificamos:** La base se encarga de avisar a la View que ahora esa propiedad tiene un error.
 ![[Pasted image 20251231023230.png]]


### 📄 6.3 Reflejo en la Vista (TelefonosView.xaml)

Para que el usuario vea el error, el `TextBox` en el XAML debe estar configurado para escuchar estas notificaciones. Usamos dos propiedades en el Binding:

- **`ValidatesOnNotifyDataErrors=True`**: Le dice al TextBox que haga caso a los errores que vienen del ViewModel.
 
- **`Validation.ErrorTemplate`**: Es lo visual del error,como se va a ver.Si no pones esto, WPF pone un borde rojo muy feo y básico por defecto. Al usar tu `StaticResource`(siempre que veas esto,está buscando algo arriba del xaml), estás aplicando un método personalizado para que el error sea más profesional.

![[Pasted image 20251231025533.png]]

Si usamos estas validaciones debemos quitar el `CanExecute` de la clase `RelayComand`.

### ¿Por qué quitarlo?

El `CanExecute` bloqueaba el botón (lo ponía gris) si los campos estaban vacíos. Si ahora usas la **Validación mediante Propiedades**:

1. El usuario ya ve visualmente qué está mal (el TextBox se pone en rojo).
 
2. Si dejas el `CanExecute` comprobando lo mismo, estás haciendo que el procesador trabaje doble: una vez para validar el texto y otra para validar el botón.
### ¿Qué tienes que quitar exactamente?

En tu ViewModel., en el constructor donde inicializas el comando, antes tenías esto: 
**ES UN EJEMPLO**
![[Pasted image 20251231023800.png]]

Para quitarlo, simplemente dejas el comando con la acción, sin la validación del botón:
![[Pasted image 20251231023826.png]]

#### ¿Y qué pasa con el método `CanExecuteSaveTelefonos`?

Puedes borrar el método completo. Al no pasarlo como parámetro al `RelayCommand`, el botón **siempre estará habilitado**.


----------------------------------------------------------------------------
## **Como queda la cosa**

**Antes (Con CanExecute):** El botón se pone gris y el usuario no sabe por qué.

**Ahora (Con Validación de Propiedades):**

1. El usuario escribe un número de 20 cifras.
 
2. El `set` de la propiedad detecta el error y llama a `AddError`.
 
3. El TextBox se pone en rojo (gracias al `ErrorTemplate` que tienes).
 
4. El usuario ve un mensaje de error claro.
 
5. El botón de guardar sigue activo, pero tú en el código controlas que si hay errores (`HasErrors`), no se guarde.