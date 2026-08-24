**Box2D** es un motor de físicas de cuerpos rígidos 2D ampliamente usado en videojuegos. LibGDX lo incluye como extensión oficial. Los conceptos clave son:


![[box2d_conceptos_fundamentales.svg|697]]
* **World:** El `World` no es el mundo visual de tu juego (eso lo gestiona LibGDX con cámaras y sprites). El `World` es únicamente la **simulación física paralela**. Es como una capa invisible encima de tu juego donde Box2D lleva la cuenta de quién pesa qué, dónde está cada cuerpo, qué gravedad hay, y qué choca con qué.

	Dentro del `World` solo metes **`Body`** (cuerpos físicos). Nada más. No metes sprites, no metes texturas, no metes sonidos. Solo cuerpos físicos. Luego tú, en tu código de juego, dices "el sprite de mi personaje se dibuja donde me diga el `Body` de mi personaje". Es decir, el `World` manda la posición, y tú dibujas encima.

* **Body:** Son los objetos físicos dentro del World. Hay tres tipos y es importante entender la diferencia:

	- **_Estático_:** No se mueve nunca, ni aunque le caigas encima. Sirve para el suelo, paredes, plataformas fijas.
	- **_Cinemático_:** Tú lo mueves manualmente con código, pero la física no lo empuja. Útil para plataformas que se mueven en bucle.
	- **_Dinámico_:** Le afecta la gravedad, los choques, las fuerzas. Es tu personaje, una bola, una caja que cae.

* **Fixture:** Un `Body` por sí solo no tiene forma ni peso. La `Fixture` es la que le dice: "este cuerpo pesa esto, tiene esta fricción, rebota así. Sin fixture, el body existe en el mundo pero no colisiona con nada,porque no tiene hitbox,el fixture añade al hitbox las propiedades físicas. El body es solo la entidad física nada más.

* **Shape:** Es la forma geométrica de la fixture (su hitbox). Los más usados son `PolygonShape` para rectángulos y `CircleShape` para círculos. Hay también `ChainShape` para terrenos irregulares.

* **Joint:** El `Joint` une dos `Body` con algún tipo de restricción mecánica. La pregunta clave es: ¿quieres que los dos objetos se muevan juntos de alguna forma concreta? Si sí, usas un `Joint`.

	Ejemplos claros:
	
	_RevoluteJoint_ (bisagra/pivote) → una puerta que gira en su bisagra, las ruedas de un coche unidas al chasis, el brazo de un personaje unido al cuerpo. Dos cuerpos que rotan uno respecto al otro en un punto fijo.
	
	_PrismaticJoint_ (carril) → un ascensor que solo puede subir y bajar, una plataforma que solo se mueve horizontalmente. Dos cuerpos donde uno se desliza sobre el otro en una sola dirección.
	
	_DistanceJoint_ (cuerda rígida) → dos cuerpos que siempre mantienen la misma distancia entre sí, como si los uniera una barra invisible.
	
	_RopeJoint_ (cuerda flexible) → dos cuerpos que no pueden alejarse más de cierta distancia, pero sí acercarse. Como un personaje colgado de una cuerda.
	
	**Tu ejemplo de pared y ventana**: no usarías `Joint`. Una ventana incrustada en una pared que no se mueve de forma independiente simplemente sería el mismo `Body` con varios `Fixture` de distintas formas, o directamente la pared es un `Body` estático con la forma que tenga. El `Joint` es para cuando tienes **dos cuerpos que se mueven y quieres restringir cómo se mueven uno respecto al otro**. Si los dos objetos son estáticos y no van a moverse nunca de forma independiente, no hay `Joint` que valga.
![[Físicas de Box2D.png]]

* **ContactListener:** Es un detector de eventos. Le dices a Box2D avísame cuando dos cosas se toquen (colisionen). Perfecto para saber cuándo el jugador pisa el suelo, o cuando una bala impacta un enemigo, recoge una moneda...

