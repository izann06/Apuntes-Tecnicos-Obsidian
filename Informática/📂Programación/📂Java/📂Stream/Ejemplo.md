import java.util.*;
import java.util.stream.*;

public class Main {

 // Clase interna para representar un estudiante
 static class Student {
 private String name;
 private String course;
 private double grade;
 private int age;

 public Student(String name, String course, double grade, int age) {
 this.name = name;
 this.course = course;
 this.grade = grade;
 this.age = age;
 }

 public String getName() { return name; }
 public String getCourse() { return course; }
 public double getGrade() { return grade; }
 public int getAge() { return age; }

 @Override
 public String toString() {
 return name + " (" + course + ", " + grade + ", " + age + ")";
 }
 }

 public static void main(String[] args) {
 List<Student> students = List.of(
 new Student("Ana", "DAM", 8.5, 19),
 new Student("Juan", "DAW", 6.0, 21),
 new Student("Lucía", "DAM", 9.2, 20),
 new Student("Pedro", "DAW", 5.4, 22),
 new Student("Marta", "DAM", 7.8, 19),
 new Student("Carlos", "ASIR", 8.1, 23)
 );

 System.out.println("1️⃣ Mostrar todos los alumnos (forEach)");
 students.stream().forEach(System.out::println);

 System.out.println("\n2️⃣ Filtrar alumnos con nota >= 8 (filter)");
 students.stream()
.filter(s -> s.getGrade() >= 8)
.forEach(System.out::println);

 System.out.println("\n3️⃣ Pasar todos los nombres a mayúsculas (map)");
 students.stream()
.map(Student::getName)
.map(String::toUpperCase)
.forEach(System.out::println);

 System.out.println("\n4️⃣ Ordenar por nota descendente (sorted)");
 students.stream()
.sorted(Comparator.comparing(Student::getGrade).reversed())
.forEach(System.out::println);

 System.out.println("\n5️⃣ Eliminar duplicados de un Stream (distinct)");
 Stream.of("A","B","A","C").distinct().forEach(System.out::println);

 System.out.println("\n6️⃣ Saltar y limitar resultados (skip, limit)");
 students.stream()
.skip(1)
.limit(3)
.forEach(System.out::println);

 System.out.println("\n7️⃣ Obtener la nota media (mapToDouble + average)");
 OptionalDouble avg = students.stream()
.mapToDouble(Student::getGrade)
.average();
 avg.ifPresent(a -> System.out.println("Nota media: " + a));

 System.out.println("\n8️⃣ Obtener edad mínima y máxima (mapToInt + min/max)");
 IntStream ages = students.stream().mapToInt(Student::getAge);
 OptionalInt minAge = ages.min();
 minAge.ifPresent(m -> System.out.println("Edad mínima: " + m));

 // Para usar max, necesitamos crear otro IntStream (ya que los streams solo se pueden consumir una vez)
 OptionalInt maxAge = students.stream().mapToInt(Student::getAge).max();
 maxAge.ifPresent(m -> System.out.println("Edad máxima: " + m));

 System.out.println("\n9️⃣ Comprobar condiciones (anyMatch, allMatch, noneMatch)");
 boolean algunoSuspenso = students.stream().anyMatch(s -> s.getGrade() < 5);
 boolean todosAprobados = students.stream().allMatch(s -> s.getGrade() >= 5);
 boolean ningunoMayor25 = students.stream().noneMatch(s -> s.getAge() > 25);
 System.out.println("Alguno suspenso: " + algunoSuspenso);
 System.out.println("Todos aprobados: " + todosAprobados);
 System.out.println("Ninguno >25: " + ningunoMayor25);

 System.out.println("\n🔟 Primer alumno del stream (findFirst)");
 students.stream()
.findFirst()
.ifPresent(s -> System.out.println("Primero: " + s));

 System.out.println("\n1️⃣1️⃣ Suma total de edades (reduce)");
 int totalEdad = students.stream()
.map(Student::getAge)
.reduce(0, (a, b) -> a + b);
 System.out.println("Suma total edades: " + totalEdad);

 System.out.println("\n1️⃣2️⃣ Agrupar alumnos por curso (groupingBy)");
 Map<String, List<Student>> porCurso = students.stream()
.collect(Collectors.groupingBy(Student::getCourse));
 porCurso.forEach((curso, lista) -> System.out.println(curso + " -> " + lista));

 System.out.println("\n1️⃣3️⃣ Calcular media por curso (groupingBy + averagingDouble)");
 Map<String, Double> mediaPorCurso = students.stream()
.collect(Collectors.groupingBy(
 Student::getCourse,
 Collectors.averagingDouble(Student::getGrade)
 ));
 mediaPorCurso.forEach((c, m) -> System.out.println(c + ": " + m));

 System.out.println("\n1️⃣4️⃣ Crear mapa nombre → nota (toMap)");
 Map<String, Double> mapaNotas = students.stream()
.collect(Collectors.toMap(
 Student::getName,
 Student::getGrade
 ));
 mapaNotas.forEach((n, nota) -> System.out.println(n + " → " + nota));

 System.out.println("\n1️⃣5️⃣ Crear lista de nombres separados por coma (joining)");
 String listaNombres = students.stream()
.map(Student::getName)
.collect(Collectors.joining(", "));
 System.out.println(listaNombres);

 System.out.println("\n1️⃣6️⃣ Obtener estadísticas de notas (summaryStatistics)");
 DoubleSummaryStatistics stats = students.stream()
.mapToDouble(Student::getGrade)
.summaryStatistics();
 System.out.println(stats);

 System.out.println("\n1️⃣7️⃣ Ejemplo de flatMap (listas dentro de listas)");
 List<List<String>> modulos = List.of(
 List.of("Programación", "Entornos"),
 List.of("Bases de Datos", "Sistemas")
 );
 modulos.stream()
.flatMap(List::stream)
.forEach(System.out::println);

 System.out.println("\n1️⃣8️⃣ Usar peek para depurar (peek)");
 students.stream()
.peek(s -> System.out.println("Procesando: " + s.getName()))
.filter(s -> s.getGrade() >= 8)
.forEach(s -> System.out.println("Aprobado alto: " + s.getName()));
 }
}
