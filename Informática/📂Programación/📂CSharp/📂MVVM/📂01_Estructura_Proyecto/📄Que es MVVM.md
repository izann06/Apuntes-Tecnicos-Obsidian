El patrón de diseño **MVVM** (Model-View-ViewModel). Es el estándar de la industria para trabajar con WPF y C#.

MVVM es una forma de organizar el código dividiéndolo en tres capas independientes.

* View(Vista)

* ViewModel(Lógica)

* Model(Datos)

El esquema del MVVM es el siguiente:
![[Pasted image 20251230202943.png]]

Se hace para separar la **Interfaz de Usuario** (lo que se ve) de la **Lógica de Negocio** (lo que el programa hace).

Esto sirve para que el proyecto sea **escalable** (pueda crecer sin volverse un caos) y **mantenible** (si algo falla, sepas exactamente en qué capa está el error). 
Además, permite que un diseñador trabaje en la vista mientras un programador trabaja en la lógica sin estorbarse.
