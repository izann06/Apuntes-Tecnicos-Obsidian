En esta carpeta creamos clases (como `ServiceTelefono.cs`) cuya única función es realizar las operaciones **CRUD** (Create, Read, Update, Delete) contra SQL Server.

### 📄 5.1 ¿Por qué un Service y no hacerlo en el ViewModel?

Podríamos poner el código de guardar directamente en el ViewModel, pero eso sería un error. Separamos el **Service** por dos razones:

1. **Limpieza:** El ViewModel solo tiene que decir "guarda esto", sin preocuparse de si la base de datos es SQL Server, un archivo de texto o una nube.
 
2. **Reutilización:** Si mañana creas otra ventana que también necesita listar teléfonos, no tienes que repetir el código; simplemente llamas al mismo servicio.
 

### 📄 5.2 El contenido del Service (Métodos CRUD)

Aquí usamos el **DbContext** que definimos en el Model. Los métodos suelen ser **asíncronos** (`async Task`) para que la aplicación no se quede congelada mientras espera a la base de datos.

- **Listar():** Entra en el túnel (`DbContext`), coge todos los registros y los devuelve como una lista.
 
- **Insertar(Telefono t):** Recibe el objeto que el ViewModel ha rellenado y lo añade a la base de datos.
 
- **Actualizar/Borrar:** Busca el registro por su clave primaria (`Ntelefono`) y aplica los cambios o lo elimina.
 

---

## 🔗 ¿Cómo se conecta todo? (El flujo completo)

1. **View:** El usuario pulsa el botón "Aceptar". Este botón está vinculado a un **Command** en el ViewModel.
 
2. **ViewModel:** El Command ejecuta un método (ej. `PerformInsertar`). Este método crea un objeto `nuevoTelefono` con los datos que el usuario escribió.
 
3. **Service:** El ViewModel llama al servicio: `var resultado = await servicio.Insertar(nuevoTelefono);`.
 
4. **Model (DbContext):** El servicio usa el **DbContext** para empujar ese objeto a SQL Server.
 
5. **Resultado:** El servicio le dice al ViewModel "todo ok", y el ViewModel lanza un `MessageBox` a la View avisando al usuario.
 

---

