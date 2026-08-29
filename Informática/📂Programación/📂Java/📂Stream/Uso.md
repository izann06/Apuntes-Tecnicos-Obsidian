## 2️⃣ Operaciones intermedias (no terminales)

> Transforman los elementos, pero **no ejecutan** el stream hasta que haya operación terminal.

| Método | Qué hace | Ejemplo |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `filter(Predicate<T>)` | Filtra elementos según condición | ![[Pasted image 20251020101647.png]] |
| `map(Function<T,R>)` | Transforma cada elemento | ![[Pasted image 20251020101734.png]] |
| `map(Function<T,R>)` (varias formas) | Combinar campos, llamar métodos | ![[Pasted image 20251020101919.png]] |
| `mapToInt` `mapToDouble´ `mapToLong´ | Convierte a stream de primitivos | ![[Pasted image 20251020102204.png]]![[Pasted image 20251020102303.png]]![[Pasted image 20251020102344.png]] |
| `flatMap(Function<T,Stream<R>>)` | Aplana estructuras anidadas | ![[Pasted image 20251020103121.png]] |
| `distinct()` | Elimina duplicados | `java Stream.of(1,2,2,3).distinct().forEach(System.out::println);` |
| `sorted()` | Ordena de forma natural | `java Stream.of("z","a").sorted().forEach(System.out::println);` |
| `sorted(Comparator)` | Orden personalizado | `java Stream.of("z","a").sorted(Comparator.reverseOrder()).forEach(System.out::println);` |
| `limit(n)` | Toma los primeros n elementos | `java Stream.of(1,2,3,4).limit(2).forEach(System.out::println); // 1 2` |
| `skip(n)` | Salta los primeros n elementos | `java Stream.of(1,2,3,4).skip(2).forEach(System.out::println); // 3 4` |
| `peek(Consumer<T>)` | Para debug, ver elementos sin consumir | `java Stream.of(1,2,3).peek(System.out::println).map(x->x*2).toList();` |

---

## 3️⃣ Operaciones terminales

> Ejecutan el stream y devuelven **resultado final**.

|Método|Qué hace|Tipo que devuelve|Ejemplo|
|---|---|---|---|
|`forEach(Consumer)`|Recorre y ejecuta acción|`void`|`java Stream.of("a","b").forEach(System.out::println);`|
|`count()`|Cuenta elementos|`long`|`java long c = Stream.of(1,2,3).count();`|
|`collect(Collector)`|Acumula resultados en colección|`List/Set/Map`|`java List<String> l = Stream.of("a","b").collect(Collectors.toList());`|
|`toList()` (Java 16+)|Atajo de collect|`List<T>`|`java List<Integer> l = Stream.of(1,2).toList();`|
|`findFirst()`|Primer elemento|`Optional<T>`|`java Optional<String> first = Stream.of("x","y").findFirst(); first.ifPresent(System.out::println);`|
|`findAny()`|Algún elemento (útil en paralelo)|`Optional<T>`|`java Stream.of("x","y").parallel().findAny().ifPresent(System.out::println);`|
|`min(Comparator)`|Valor mínimo|`Optional<T>`|`java Optional<Integer> min = Stream.of(3,1,2).min(Integer::compare);`|
|`max(Comparator)`|Valor máximo|`Optional<T>`|`java Optional<Integer> max = Stream.of(3,1,2).max(Integer::compare);`|
|`anyMatch(Predicate)`|True si algún elemento cumple|`boolean`|`java boolean b = Stream.of(1,2,3).anyMatch(x->x>2);`|
|`allMatch(Predicate)`|True si todos cumplen|`boolean`|`java boolean b = Stream.of(1,2,3).allMatch(x>0);`|
|`noneMatch(Predicate)`|True si ninguno cumple|`boolean`|`java boolean b = Stream.of(1,2,3).noneMatch(x->x<0);`|
|`reduce(identity, BinaryOperator)`|Combina todos los elementos|`T`|`java int sum = Stream.of(1,2,3).reduce(0,(a,b)->a+b);`|
|`reduce(BinaryOperator)`|Combina en Optional|`Optional<T>`|`java Optional<Integer> sum = Stream.of(1,2,3).reduce((a,b)->a+b);`|

---

## 4️⃣ Operaciones numéricas

| Método | Qué hace | Tipo | Ejemplo |
| --------------------- | ------------------------- | -------------------------------------------------- | ---------------------------------------------------------------------------- |
| `sum()` | Suma valores | primitivo | `java int total = IntStream.of(1,2,3).sum();` |
| `average()` | Media | `OptionalDouble` | ![[Pasted image 20251020102027.png]] |
| `min()` | Valor mínimo | `OptionalInt/Double/Long` | `java OptionalInt min = IntStream.of(1,2,3).min();` |
| `max()` | Valor máximo | `OptionalInt/Double/Long` | `java OptionalInt max = IntStream.of(1,2,3).max();` |
| `summaryStatistics()` | count, sum, min, max, avg | `IntSummaryStatistics` / `DoubleSummaryStatistics` | `java IntSummaryStatistics stats = IntStream.of(1,2,3).summaryStatistics();` |

---

## 5️⃣ Collectors más usados

|Collector|Qué hace|Ejemplo|
|---|---|---|
|`toList()`|Lista|`.collect(Collectors.toList())`|
|`toSet()`|Conjunto|`.collect(Collectors.toSet())`|
|`joining(", ")`|Une strings|`.collect(Collectors.joining(", "))`|
|`counting()`|Cuenta elementos|`.collect(Collectors.counting())`|
|`summingDouble(...)`|Suma valores|`.collect(Collectors.summingDouble(Product::getPrice))`|
|`groupingBy(...)`|Agrupa por clave|`.collect(Collectors.groupingBy(Product::getCategory))`|
|`partitioningBy(...)`|Divide en 2 grupos|`.collect(Collectors.partitioningBy(p -> p.getPrice() > 100))`|
|`mapping(...)`|Map dentro de collect|`.collect(Collectors.mapping(Product::getName, Collectors.toList()))`|