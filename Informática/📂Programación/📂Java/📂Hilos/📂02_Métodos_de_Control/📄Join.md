
```java
package org.example.Ejercicio1; 
 
public class App { 
 public static void main(String[] args) { 
 
 // CORREDOR 1: Es rápido (tarda 2 seg) 
 Thread corredor1 = new Thread(() -> { 
 System.out.println("🏃 Corredor 1: ¡Sal!"); 
 try { Thread.sleep(2000); } catch (Exception e){} 
 System.out.println("🏁 Corredor 1: ¡LLEGUÉ!"); 
 }); 
 
 // CORREDOR 2: Es un poco más lento (tarda 4 seg) 
 Thread corredor2 = new Thread(() -> { 
 System.out.println("🏃 Corredor 2: ¡Sal!"); 
 try { Thread.sleep(4000); } catch (Exception e){} 
 System.out.println("🏁 Corredor 2: ¡LLEGUÉ!"); 
 }); 
 
 // 1. EL ENTRENADOR (MAIN) DA LA SALIDA 
 corredor1.start(); 
 corredor2.start(); 
 
 System.out.println("ENTRENADOR: Ya están corriendo. Me espero."); 
 
 try { 
 // 2. Esperamos al primero 
 corredor1.join(); 
 System.out.println("ENTRENADOR: He visto llegar al 1."); 
 
 // 3. Esperamos al segundo 
 corredor2.join(); 
 System.out.println("ENTRENADOR: He visto llegar al 2."); 
 
 } catch (InterruptedException e) { 
 e.printStackTrace(); 
 } 
 
 // 4. SOLO SE IMPRIME ESTO CUANDO LOS DOS HAN TERMINADO 
 System.out.println("ENTRENADOR: Carrera terminada."); 
 } 
}

```