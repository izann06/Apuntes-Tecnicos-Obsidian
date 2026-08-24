### 🔴 SÍ tienes que cerrar (Llamar a `dispose()`)

Cualquier objeto en LibGDX que implemente la interfaz `Disposable`. Si Android Studio te deja escribir `.dispose()` después del nombre de la variable, casi seguro que tienes que usarlo.

1. **Herramientas de Dibujo:** `SpriteBatch`, `ShapeRenderer`, `OrthogonalTiledMapRenderer`, `Box2DDebugRenderer`. (Son los pinceles y lienzos).
    
2. **Mundos Físicos:** El `World` de Box2D. (Oculta mucha memoria en C++).
    
3. **Formas Geométricas (Shapes):** ¡Cuidado aquí! Cuando creas un cuadrado o un círculo para Box2D (`PolygonShape` o `CircleShape`), tienes que llamar a `shape.dispose()` **justo después de aplicarlo al cuerpo**, no al final del juego. (Si usas el DSL de `ktx-box2d`, esto lo hace automático por ti).
    
4. **Interfaces de Usuario (Scene2D):** El `Stage` (tu HUD) y las fuentes personalizadas (`BitmapFont`, `FreeTypeFontGenerator`).
    
5. **Efectos Visuales:** `ParticleEffect`.
    

---

### 🟢 NO tienes que cerrar (¡Prohibido tocar!)

Aquí es donde la mayoría de los programadores novatos cometen errores fatales. Hay cosas que **no debes destruir tú**, porque tienen un dueño o se limpian solas.

**1. Los recursos cargados por el `AssetManager` (¡La trampa más común!)** Mira tu `GameScreen.kt`. Tienes el mapa, la música y el atlas:

```Kotlin
val atlas = game.assets.get("atlas/juego.atlas", TextureAtlas::class.java)
val musica = game.assets.get("audio/musica.ogg", Music::class.java)
```

**NUNCA pongas `atlas.dispose()` o `musica.dispose()` en tu pantalla de juego.**

- **¿Por qué?** Porque el dueño de esos archivos es el `AssetManager` (que vive en tu clase `KotlinGameMain`). Si tú destruyes el atlas en la pantalla de juego y el jugador vuelve al menú, el juego explotará porque el menú intentará usar un atlas que tú has tirado a la basura.
    
- **¿Quién lo limpia?** El `AssetManager` lo destruye TODO de golpe cuando cierras la aplicación por completo (`assets.dispose()` en el Main).
    

**2. Cosas que te han "prestado"** En tu `GameScreen` usas `game.batch` para dibujar. No se te ocurra hacer `game.batch.dispose()` al salir de la pantalla de juego. El pincel es del `KotlinGameMain` (el jefe), y lo va a necesitar para dibujar la pantalla de _Game Over_.

**3. Variables normales de Kotlin** Textos (`String`), números (`Int`, `Float`), Vectores matemáticos (`Vector2`, `Vector3`), listas lógicas (`mutableListOf<Moneda>`). Todo esto es puro Kotlin. De esto sí se encarga el camión de la basura automático (Garbage Collector) de Android. Te olvidas de ellos.

---

### Resumen visual de tu `GameScreen`

Para que te quede clarísimo, mira cómo debería ser el método `dispose()` de tu pantalla de juego basándonos en estas reglas:

```Kotlin
override fun dispose() {
    // SÍ SE CIERRAN (Porque los has creado TÚ con la palabra "new" o instanciando dentro de esta pantalla):
    worldManager.dispose()    // Cierra las físicas
    gestorPart.dispose()      // Cierra las partículas (las texturas que creaste por código)
    hud.dispose()             // Cierra el Stage de la interfaz
    debugRenderer.dispose()   // Cierra las gafas de rayos X
    mapRenderer.dispose()     // Cierra el dibujante del mapa

    // ❌ NO SE CIERRAN AQUÍ (Son del AssetManager o prestados del Main):
    // atlas.dispose()
    // musica.dispose()
    // sfxSalto.dispose()
    // tiledMap.dispose()
    // game.batch.dispose()
}
```