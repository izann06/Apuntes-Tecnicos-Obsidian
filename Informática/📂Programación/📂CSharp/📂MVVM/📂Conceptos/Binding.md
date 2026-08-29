El **binding** es la “conexión automática” entre:

1. **El objeto que estás editando** (por ejemplo, `usuarioSeleccionado`).En este caso IzanM.

	![[Binding.png]]

2. **Los controles de la UI** (TextBox, ListBox, etc.).
![[Binding-1.png]]
 

Esto significa que:

- Cuando seleccionas un usuario en el ListBox, los TextBox del panel derecho **muestran automáticamente sus datos**.
 
- Cuando modificas los TextBox, los cambios **se guardan directamente en el objeto** sin necesidad de escribir código extra.
 
- Gracias a `INotifyPropertyChanged`, cualquier cambio en las propiedades del usuario también se refleja **instantáneamente en el ListBox** si se está mostrando allí.