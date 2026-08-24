
#### **1. El uso de `synchronized`**

El **`synchronized`** se usa en el método `processBid` porque varios clientes van a usar ese método a la vez. Como se va a enviar un objeto `Bid` y el servidor tiene que procesarlo, si no aplicamos el `synchronized`, los valores de los atributos se podrían corromper o perder por el camino. Lo que hace este modificador es obligar a los hilos a entrar **uno por uno**.

- **Ejemplo de la "Libreta del Subastador":** Imagina que el precio actual es **1000€**.
    
    1. El **Jugador A** puja **1200€** y el **Jugador B** puja **1300€** casi al mismo tiempo.
        
    2. Sin `synchronized`, ambos hilos ven que 1000€ es el precio actual y los dos creen que su puja es válida.
        
    3. El Jugador B escribe en la libreta: "Líder B con 1300€".
        
    4. Pero el Jugador A, que ya había pasado la validación, escribe encima justo después: "Líder A con 1200€". **Resultado:** El ganador acaba siendo el que ofreció menos dinero porque su hilo terminó un poco después. El `synchronized` evita esto haciendo que hagan cola.
        

---

#### **2. El uso de `CopyOnWriteArrayList`**

El **`CopyOnWriteArrayList`** lo que hace es que, cada vez que la lista se quiera modificar desde un hilo (por ejemplo, cuando se conecta un cliente nuevo), no modifica de primeras la lista original, sino que hace una **copia**. Hace lo que tenga que hacer en esa copia y, al terminar, la aplica a la lista normal.

De esta forma, **no interrumpe a los demás métodos** (como el que envía los mensajes a todos los clientes) que puedan estar usando la lista al mismo tiempo. Así evitamos que salte una excepción porque varios métodos toquen la misma lista a la vez.