En Hibernate, cuando una tabla tiene claves foráneas (relaciones), tienes que elegir cómo quieres que se traigan esos datos "extra".

#### 1. LAZY (El modo rápido y recomendado)

Es el modo **perezoso**. Cuando pides un objeto (ej. un Libro), Hibernate **solo** te trae los datos de ese libro. No se trae al Autor ni nada de otras tablas.

- **¿Por qué se usa?** Porque es muchísimo más **rápido**. No sobrecarga la memoria con datos que a lo mejor ni vas a usar.
 
- **El truco (JOIN FETCH):** Si de repente necesitas los datos de la otra tabla, lo más profesional en proyectos grandes es usar un `JOIN FETCH` en tu consulta. Así le dices: _"Oye, normalmente eres vago, pero para esta vez tráeme también al Autor de un solo viaje"_. Es la forma más limpia de trabajar.
 

#### 2. EAGER (El modo automático pero pesado)

Es el modo **ansioso**. En cuanto pides un Libro, Hibernate te trae **todo** automáticamente: el libro, el autor, y todo lo que esté conectado a ellos.

- **¿Cuál es el problema?** Que es mucho más **lento**. En un proyecto con miles de datos, si todo fuera Eager, la aplicación iría "a pedales" porque cada vez que pidas una cosa, Hibernate intentará traerse media base de datos de golpe.
 

---

### 💡 Resumen para estudiar:

- **LAZY:** Solo trae lo que pides. Es **más rápido**. Si quieres lo demás, usas `JOIN FETCH`. Es lo que se usa en **proyectos grandes** para que no explote el rendimiento.
 
- **EAGER:** Te lo trae todo de golpe sin preguntar. Es **más lento** y pesado, aunque sea "más cómodo" porque te olvidas de hacer joins.