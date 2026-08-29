La función del `synchronized` es que cuando hayan muchos hilos que tengan que entrar a un método(cumpliendo unas instrucciones),lo hagan de uno en uno para no liarse y mostrar errores.

Lo de cumpliendo unas instrucciones me refiero a que no siempre que tengamos un método en el uqe vayan a ejecutarlo 1000 hilos hay que usarlo si no que debe cumplir lo siguiente:

### La Regla de Oro: ¿Cuándo usarlo y cuándo no?

|**Situación**|**¿Usar synchronized?**|**¿Por qué?**|
|---|---|---|
|**Leer + Modificar + Escribir** (Ej: `saldo++`)|**SÍ** (Obligatorio)|Evita que dos hilos lean lo mismo y se pisen el resultado.|
|**Mostrar mensajes** (`System.out.println`)|**NO**|Java ya lo gestiona. Solo verás las líneas en orden distinto, pero no se rompe nada.|
|**Variables locales** (dentro del `run`)|**NO**|Cada hilo tiene su propia copia privada. No hay riesgo de choque.|
|**Solo leer datos** (Consultar saldo)|**Casi nunca**|Si el dato no va a cambiar mientras lo lees, no hace falta bloquear a nadie.|
|**Objetos inmutables** (`final`)|**NO**|Como no se pueden cambiar, son seguros por naturaleza.|
Aquí tienes un ejemplo de que al usar un método que lee, modifica y escribe el saldo, es usado por **1000 hilos** y al **hilo Nº28** ya falla, suele fallar sobre todo si hay un `Thread.sleep` de por medio.

## **CLASE CUENTACORRUPTA**
```java
package org.example.Ejercicio2; 
 
public class CuentaCorrupta implements Runnable { 
 // Variable compartida 
 private int saldo = 0; 
 
 @Override 
 public void run() { 
 // Cada hilo intenta sumar 1 al saldo 
 sumarUno(); 
 } 
 
 // SIN SYNCHRONIZED: Los hilos se pisan 
 public void sumarUno() { 
 // 1. El hilo lee el saldo y lo guarda en una variable local 
 int copiaSaldo = this.saldo; 
 
 // 2. FORZAMOS EL FALLO: El hilo se pausa un milisegundo. 
 // Esto da tiempo a que otros CIEN hilos lean el MISMO valor de 'saldo' // antes de que este hilo pueda incrementarlo. 
 try { 
 Thread.sleep(1); 
 } catch (InterruptedException e) {} 
 
 // 3. Incrementa la copia que leyó al principio 
 copiaSaldo = copiaSaldo + 1; 
 
 // 4. Machaca el saldo real con su copia 
 this.saldo = copiaSaldo; 
 } 
 
 public int getSaldo() { 
 return saldo; 
 } 
}

```

## **MAIN**
```java
package org.example.Ejercicio2; 
 
public class App { 
 
 public static void main(String[] args) throws InterruptedException { 
 
 CuentaCorrupta tarea = new CuentaCorrupta(); 
 Thread[] hilos = new Thread[1000]; 
 
 // 1. Creamos 1000 hilos 
 for (int i = 0; i < 1000; i++) { 
 hilos[i] = new Thread(tarea); 
 } 
 
 // 2. Los lanzamos todos a la vez 
 for (int i = 0; i < 1000; i++) { 
 hilos[i].start(); 
 } 
 
 // 3. Esperamos a que TODOS terminen antes de mirar el saldo 
 for (int i = 0; i < 1000; i++) { 
 hilos[i].join(); 
 } 
 
 // 4. Resultado final 
 System.out.println("Resultado esperado: 1000"); 
 System.out.println("Resultado real: " + tarea.getSaldo()); 
 
 if (tarea.getSaldo() < 1000) { 
 System.out.println("¡FALLO DETECTADO! Se han perdido actualizaciones por falta de synchronized."); 
 } 
 } 
}
```

## **Resultado:**

![[Pasted image 20260128103755.png]]