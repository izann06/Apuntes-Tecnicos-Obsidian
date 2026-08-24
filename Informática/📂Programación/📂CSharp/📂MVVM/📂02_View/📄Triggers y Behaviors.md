Los triggers se usan para **controles que NO tienen la propiedad `Command`**. 

Un botón si tiene la propiedad command por lo que NO hay que aplicar un trigger para este.
Para los eventos como (Loaded,SelectionChanged,MouseEnter...) SI se usan, ya que no tienen la propiedad `command`.

Antes los eventos los hacíamos en el code behind, pero con el viewmodel, eso está prohibido. Ahora los métodos que estaban en el code behind están en el viewmodel.

Por lo que, la solución es aplicar estos triggers que son los responsables en llamar a los comandos ( que están en el vm) que contendrán los métodos que buscamos como al hacer click en un botón. 


## Para aplicar los triggers debes descargarte este plugin:

**Microsoft.Xaml.Behaviors.Wpf**

![[Pasted image 20260108073248.png]]


![[Pasted image 20260108073314.png]]

## Si quieres aplicarlo en una `View` debes llamarlo de esta manera:

**xmlns:i="clr-namespace:Microsoft.Xaml.Behaviors;assembly=Microsoft.Xaml.Behaviors"**
![[Pasted image 20260108073705.png]]

## Ahora aplicamos el trigger.
Pongo un ejemplo que sirve para cargar unos objetos por pantalla:

![[Pasted image 20260108073806.png]]

El evento es Loaded,que se ejecutará al abrir la view y llamará al comando `CargarCommand`que se encuentra en la viewmodel de esta view y contiene el método pata cargar la lista de objetos.
![[Pasted image 20260108073945.png]]