Para cumplir con la **Clean Architecture** y el patrón MVVM, nunca debemos llamar a la base de datos (DAO) directamente desde la pantalla o el ViewModel. Necesitamos intermediarios.

## 1. LocalDatasource

Su única responsabilidad es envolver al DAO. Si mañana cambiamos ROOM por otra base de datos (como Realm o SQLite puro), solo tendríamos que tocar este archivo.

En este ejemplo, por motivos didácticos, **exponemos los datos de dos formas**: usando `Flow` (lo moderno) y `LiveData` (lo clásico).

![[Pasted image 20260114140527.png]]

---

## 2. Repository

El Repositorio es la cara visible para el ViewModel.

Aunque en este ejemplo parezca "código repetido" (porque solo llama al Datasource), su función real es **centralizar**. Si tuviéramos una API (Retrofit), el Repositorio sería quien coordinaría: _"Primero guardo lo que viene de la API en el LocalDatasource y luego te lo muestro"_.

![[Pasted image 20260114140552.png]]

---

### Resumen del Flujo de Datos

1. **Base de Datos:** Tiene los datos crudos.
 
2. **DAO:** Sabe SQL (`SELECT *...`).
 
3. **LocalDatasource:** Abstrae el DAO.
 
4. **Repository:** Centraliza las fuentes de datos.
 
5. **ViewModel:** Pide datos al Repository y los prepara para la UI.