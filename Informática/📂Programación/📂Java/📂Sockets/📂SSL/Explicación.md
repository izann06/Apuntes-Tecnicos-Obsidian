
**SSL** (Secure Sockets Layer) es una capa de seguridad.

Si no aplicas el SSL, tus datos van por internet en texto plano, por lo que cualquier persona que intercepte tu señal wifi podrá ver con facilidad que datos estás mandando y eso es un peligro. 
Con SSL los datos se encriptan (se vuelven ilegibles) antes de salir de tu ordenador y se desencriptan cuando llega a su destino

#### Por qué está montado así? (Certificados)

Para que SSL funcione, el Servidor necesita una **Identidad**.

1. **`server.jks`**: Es el "DNI" del servidor. Contiene su clave privada.
 
2. **`System.setProperty`**: Es la forma de decirle a Java: "Oye, antes de que abras ningún enchufe, que sepas que mis credenciales están en este archivo y la contraseña es 123456".

> [!TIP] IMPORTANTE
> 
>Si quieres generar el SSL tienes que hacerlo mediante unos comandos en la terminal, pideselos a la IA te los dará sin problema,te pedirá muchas cosas dale Enter,no hace falta que rellenes nada si no es necesario,solo la contraseña y poco mas.
>

![[Explicación.png]]

Se nos generará una archivo y tendremos que colocarlo en la raiz del proyecto:
![[Explicación-2.png]]