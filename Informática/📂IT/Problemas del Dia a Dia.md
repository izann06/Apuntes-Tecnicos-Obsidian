
## 1. Al arrastrar el ratón en la pantalla, la parte arrastrada se queda completamente negra.

Esto se debe a un fallo en el refresco gráfico o de los controladores de video.

### 1.1 Intenta reiniciar el driver de video, te dejo un comando que fuerza a la GPU a reiniciarse sin cerrar tus programas.

##### **`Windows + Ctrl + Shift + B`**

### 1.2. Sombras del puntero (El culpable clásico)

A veces el sistema intenta dibujar una sombra bajo el ratón y el proceso falla, dejando ese rastro negro.

1. Pulsa la tecla **Windows** y escribe: `Ajustar la apariencia y rendimiento de Windows`.
    
2. En la lista que aparece, busca la opción **"Mostrar sombras bajo el puntero del mouse"**.
    
3. **Desmárcala** y dale a Aplicar.
    

---

### 1.3. Actualiza el controlador de pantalla

Si nada de lo anterior funcionó, es probable que tu tarjeta de video esté usando un lenguaje que Windows ya no entiende bien.

1. Haz clic derecho en el botón de Inicio y elige **Administrador de dispositivos**.
    
2. Despliega **Adaptadores de pantalla** o **Monitores**.
    
3. Haz clic derecho y selecciona **Actualizar controlador**.
    
4. Elige "Buscar controladores automáticamente".