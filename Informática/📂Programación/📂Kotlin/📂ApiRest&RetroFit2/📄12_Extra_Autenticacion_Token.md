Hasta ahora hemos usado una API pública (abierta a todo el mundo). Pero en el mundo real, la mayoría de las APIs (como la de Twitter, Spotify o la de tu empresa) son privadas. Necesitas un "carnet de socio" para entrar. Ese carnet se llama **Token**.

Cuando una API es privada, no puedes simplemente hacer un `GET` y esperar datos. El servidor te responderá con un error **401 Unauthorized** (No autorizado).

Para solucionarlo, debemos enviar una **clave especial (Token)** en la **Cabecera (Header)** de cada petición.

## 1. ¿Qué es la Cabecera (Header)?

Imagina que la petición HTTP es una carta:

- **El Body (Cuerpo):** Es la carta que va dentro del sobre (los datos del JSON).
    
- **El Header (Cabecera):** Es lo que escribes fuera del sobre (remite, sello, urgencia). Aquí es donde pegamos nuestro "sello de autorización".