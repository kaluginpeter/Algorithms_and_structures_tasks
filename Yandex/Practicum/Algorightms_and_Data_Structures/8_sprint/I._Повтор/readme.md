I. Повтор

Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод

Все языки	0.3 секунды	64Mb	стандартный ввод или input.txt	стандартный вывод или output.txt

OpenJDK Java 11	0.4 секунды	128Mb

C# (MS .NET 6.0 + ASP)	0.4 секунды	128Mb

Python 3.12.1	0.6 секунд	64Mb

Java 21 (Temurin JDK)	0.399 секунд	128Mb

Kotlin 1.8.0 (JRE 11)	0.4 секунды	128Mb

C# (MS .NET 5.0 + ASP)	0.4 секунды	128Mb

Будем говорить, что строка s является повтором длины k, если существует такая строка t, что s = t * k, 

где под умножением подразумевается конкатенация k экземпляров строки t один за другим.

Например, строка abababab является повтором строки abab длины 2,

а также повторением строки ab длины 4. Тогда имеет смысл говорить о наибольшем повторе. 

Строка является наибольшим повтором длины k, если она является повтором некоторой строки длины k

и если не существует такой строки t, что s —– повтор t длины m > k. 

Например, строка aaaa является наибольшим повтором длины 4.

Вам дана строка, которая является наибольшим повтором длины x. Найдите x.

Заметим, что ответ всегда равен хотя бы единице, так как строка является повтором самой себя.

Формат ввода

В единственной строке дана строка, состоящая из строчных букв английского алфавита

и не превышающая в длину 106. Строка не бывает пустой.

Формат вывода

Выведите единственное число — x, длину наибольшего повтора.

Пример 1

Ввод	Вывод

zzzzzz

6

Пример 2

Ввод	Вывод

abacaba

1

Пример 3

Ввод	Вывод

abababab

4
