### 🚀 1. Puesta en Marcha: App.xaml

Antes de hacer el view, debemos configurar el proyecto para que el App.xaml sepa dónde está nuestra vista, ya que al crear las carpetas hemos cambiado la ruta por defecto.

**¿Qué es el App.xaml?**

Es el punto de entrada de la aplicación. Por defecto, Visual Studio busca una ventana llamada `MainWindow.xaml` en la raíz del proyecto. Como nosotros seguimos el patrón MVVM y hemos organizado nuestras vistas en una carpeta específica, debemos hacer lo siguiente:

1. **Localiza** el archivo `App.xaml` en la raíz de tu proyecto.
 
2. **Borra** la referencia a `MainWindow.xaml`.
 
3. **Escribe** `StartupUri="View/(Nombre del archivo).xaml"`.
 

EJEMPLO:

![[Pasted image 20251230203836.png]]

---

### 🎨 2. TelefonosView.xaml (El diseño)

Aquí es donde escribes el código XAML. Para que este archivo se comunique con el ViewModel, usamos el **Binding**.

- **¿Qué es el Binding?** Es el enlace que conecta un control (como un `TextBox`) con una propiedad del ViewModel.
 
- **Ejemplo:** Si queremos que un cuadro de texto muestre el nombre del contacto, ponemos: `<TextBox Text="{Binding Nombre}" />`
 

---

### 🔌 3. El Code Behind (TelefonosView.xaml.cs)

Aunque en MVVM intentamos no escribir código aquí, hay una excepción obligatoria: **conectar el enchufe**.

Para que la Vista sepa de qué ViewModel sacar los datos, en el code behind debemos asignar el `DataContext`.


![[Pasted image 20251230204017.png]]