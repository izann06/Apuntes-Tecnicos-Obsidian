
```Kotlin
id("com.google.devtools.ksp")
```

```Kotlin
// DataStore  
implementation("androidx.datastore:datastore-preferences:1.1.7")  
  
// Navigation Compose  
implementation("androidx.navigation:navigation-compose:2.9.2")  
  
//Iconos  
implementation("androidx.compose.material:material-icons-extended")  
  
// ROOM dependencies  
implementation("androidx.room:room-runtime:2.7.2")  
implementation("androidx.room:room-ktx:2.7.2")  
ksp("androidx.room:room-compiler:2.7.2") // KSP para procesamiento de anotaciones.  
  
// ViewModel  
implementation("androidx.lifecycle:lifecycle-viewmodel-ktx:2.9.3")  
implementation("androidx.lifecycle:lifecycle-viewmodel-compose:2.9.3")  
  
// Retrofit2  
implementation("com.squareup.retrofit2:retrofit:3.0.0")  
  
// Conversor para JSON (Gson)  
implementation("com.squareup.retrofit2:converter-gson:3.0.0")  
  
// Corutinas (para llamadas asíncronas)  
implementation("org.jetbrains.kotlinx:kotlinx-coroutines-android:1.10.2")  
// Imágenes  
implementation("io.coil-kt.coil3:coil-compose:3.2.0")  
implementation("io.coil-kt.coil3:coil-network-okhttp:3.2.0")
  
```
